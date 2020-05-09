import json
import os
import ssl
import argparse
import requests
import re
from bs4 import BeautifulSoup
import configuration as c

COUNTRIES = ['it', 'nl', 'us', 'fr']

def is_new(app_id, apps):
    for a in apps:
        if(a['id'] == app_id):
            return False
    return True

def collect_data(input):
    
    for country in COUNTRIES:
        data_path = input + '/data_' + country
        if(not os.path.exists(data_path)):
            print('The country with code "' + country + '" is new, I am setting up its folder and app.json file now...')
            os.mkdir(data_path)
            os.mkdir(data_path + '/apks')
            os.mkdir(data_path + '/data')
            os.mkdir(data_path +  '/reports')
            c.save(data_path + '/apps.json', [])
        
        c.setPaths(data_path)

        url = 'https://play.google.com/store/search?q=covid&gl=' + country 
        r = requests.get(url)
        search_page = BeautifulSoup(r.text, 'html.parser')
        # We look for all the links referring to the apps listed by the search 
        apps = search_page.find_all("a", href=re.compile('^\/store\/apps\/details\?id=*'))
        app_ids = list()
        # We collect all app ids
        for a in apps:
            app_ids.append(a['href'].replace('/store/apps/details?id=', ''))
        # Remove duplicate ids
        app_ids = list(dict.fromkeys(app_ids))
        
        # Now we iterate over all apps and add the new ones to the apps.json file
        analysed_apps = json.load(open(c.APPS_PATH, 'r')) 
        for a in app_ids:
            if(is_new(a, analysed_apps)):
                analysed_apps.append({'id': a, 'store_country': country, 'store_lang': country})

        c.save(c.APPS_PATH, analysed_apps)

# We check if the provided input is correct and then we start checking and collecting the new data 
def update(input):
    
    # We don't even start if the provided path does not exist
    if(not os.path.exists(input)):
        print('Error - the provided path does not exist: ' + options.input)
        exit()

    collect_data(input)

def main():
    # Arguments definition and management
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to the folder containing the data to be updated', required=True, type=str)
    options = parser.parse_args()

    # This will allow us to trust SSL certificates from the servers we will interact with (e.g., the one for downloading NLTK stop word)
    ssl._create_default_https_context = ssl._create_unverified_context

    update(options.input)

if __name__ == "__main__":
    main()