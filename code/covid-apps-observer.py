import json
import crawler as crawler
import androguard_androwarn_analyzer
import servers_analyzer
import configuration as c

def start():

    apps = json.load(open(c.APPS_PATH, 'r'))

    for a in apps:
        # Crawl data from the Google Play store
        crawled_new_data = crawler.crawl_data(a)

        # if the app has a new release we did not analyze before...
        if(crawled_new_data):
            # Launch the Androguard and Androwarn analyses
            androguard_androwarn_analyzer.analyze(a)
            # Analyze the servers pointed by the URLs we found in the String analysis of Androguard
        servers_analyzer.analyze(a)
        
        
    # Finally, if everything goes well, save the updated apps.json file with the new timestamps and versions
    c.save(c.APPS_PATH, apps)

start()
