import json
import os
import ssl
import argparse
import requests
import re
from bs4 import BeautifulSoup
import covid_apps_observer
import configuration as c

# Check if the app with app_id is already present in the apps list
def is_new(app_id, apps):
    for a in apps:
        if(a['id'] == app_id):
            return False
    return True

# Iterates over all countries and searches for new covid apps in the Google Play store
def update_apps_lists(root_path, countries):
    
    for e in countries:
        country = e['code']
        lang = e['lang']
        data_path = root_path + '/data_' + country
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

def analyze_apps(root_path, author_name, author_email, countries):
    # We launch the analysis for each country
    for e in countries:
        country = e['code']
        country_name = e['name']
        data_path = root_path + '/data_' + country
        if os.path.exists(data_path) and os.path.exists(data_path + '/apps.json'):
            covid_apps_observer.run_analysis(data_path, author_name, author_email, 'COVID-related Android apps in ' + country_name)

def main():
    # Arguments definition and management
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to the folder containing the data to be updated and the countries.json file', required=True, type=str)
    parser.add_argument('-an', '--author_name', help='Name of the author of the analysis', required=False, type=str)
    parser.add_argument('-ae', '--author_email', help='Email address of the author of the analysis', required=False, type=str)
    options = parser.parse_args()

    # This will allow us to trust SSL certificates from the servers we will interact with (e.g., the one for downloading NLTK stop word)
    ssl._create_default_https_context = ssl._create_unverified_context

    # We don't even start if the provided path does not exist
    if not os.path.exists(options.input) or not os.path.exists(options.input + '/countries.json'):
        print('Error - the provided path does not exist: ' + options.input)
        exit()

    countries = json.load(open(options.input + '/countries.json', 'r'))

    update_apps_lists(options.input, countries)
    analyze_apps(options.input, options.author_name, options.author_email, countries)

if __name__ == "__main__":
    main()