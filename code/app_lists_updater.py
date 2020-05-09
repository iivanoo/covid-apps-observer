import json
import os
import ssl
import argparse
import requests
import re
from bs4 import BeautifulSoup
import configuration as c

COUNTRIES = [
    {'country_code': 'it', 'lang': 'it'},
    {'country_code': 'nl', 'lang': 'nl'},
    {'country_code': 'us', 'lang': 'us'},
    {'country_code': 'fr', 'lang': 'fr'},
    {'country_code': 'uk', 'lang': 'en'},
    {'country_code': 'de', 'lang': 'de'},
    {'country_code': 'es', 'lang': 'es'},
    {'country_code': 'gr', 'lang': 'gr'},
    {'country_code': 'ar', 'lang': 'es'},
    {'country_code': 'br', 'lang': 'pt'},
    {'country_code': 'ca', 'lang': 'en'},
    {'country_code': 'cn', 'lang': 'en'},
    {'country_code': 'in', 'lang': 'in'},
    {'country_code': 'jp', 'lang': 'jp'},
    {'country_code': 'ru', 'lang': 'ru'},
    {'country_code': 'au', 'lang': 'en'},
    ]

# Check if the app with app_id is already present in the apps list
def is_new(app_id, apps):
    for a in apps:
        if(a['id'] == app_id):
            return False
    return True

def collect_data(input):
    
    for e in COUNTRIES:
        country = e['country_code']
        lang = e['lang']
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
                analysed_apps.append({'id': a, 'store_country': country, 'store_lang': lang})

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