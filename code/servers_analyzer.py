import re
import lib.whois as whois
from tld import get_tld
import configuration as c


# Applies a black-list based heuristics which returns True if the url is a good candidate for beging a relevant one
def is_candidate(url):
    if re.search('http:\/\/%', url):
        return False
    if re.search('https:\/\/%', url):
        return False
    if re.search('\*', url):
        return False
    if re.search('schema', url):
        return False
    if re.search('localhost', url):
        return False
    if re.search('127.0.0.1', url):
        return False
    if re.search('example', url):
        return False
    if re.search('hostname', url):
        return False
    # if the url is too short, we discard it
    if len(url.replace('http://', '').replace('https://', '')) <= 2:
        return False
    return True


# Given a url, it returns only its first-level domain
def get_first_level_domain(url):
    try:
        res = get_tld(url, as_object=True)
        return res.fld
    except:
        return None


# Checks all the URLs managed within the app and returns the candidates for being relevant URLs
def get_candidate_urls(app):
    result = list()
    
    # Get all candidates URLs from the json file produced by the Androguard analyzer
    all_urls = c.get_raw_data(app, 'androguard')['urls']
    
    # Here we check if the data is actually there, otherwise we skip the analysis
    if(all_urls is None):
        return
    
    for current_url in all_urls:
        if is_candidate(current_url):
            polished_url = get_first_level_domain(current_url)
            if not polished_url is None:
                result.append(polished_url)
    
    # Remove duplicates
    result = list(dict.fromkeys(result))
    return result


# Polishes the list of URLs used in the app and performs a whois lookup on the most promising ones
def analyze(app):
    print('Analyzing the servers mentioned by: ' + app['id'])
    result = list()
    urls = get_candidate_urls(app)

    for url in urls:
        # Here is where we do the real Whois query
        try:
            domain_info = whois.query(url, force=1, slow_down=2)
            # We transform the domain object into a plain dictionary, otherwise we cannot save it into the json file
            item = domain_info.__dict__
            result.append(item)
        except:
            print('Error performing the whois lookup for this server, it will be ignored: ' + url)

    # We save the result into a JSON file
    app_suffix_path = app['id'] + c.SEPARATOR + app['latest_crawled_version']
    result_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'servers.json' 
    c.save(result_path, result)