import time
import json
import sys
import os
import time
from google_play_scraper import app
import ssl
import configuration as c
import apk_downloader

def download_apk(app_to_download, apk_path):
    print('Downloading the APK of: ' + app_to_download)
    return apk_downloader.download_apk(app_to_download, apk_path)
    

def get_gp_metadata(app_to_scrape):
    ssl._create_default_https_context = ssl._create_unverified_context
    app_metadata = app(app_to_scrape['id'], lang='en', country=app_to_scrape['store_country'])
    return app_metadata

def start():

    apps = json.load(open(c.apps_path, 'r'))

    for a in apps:
        # Download Google Play metadata
        app_metadata = get_gp_metadata(a)
        app_latest_version = app_metadata['version']
        app_suffix_path = a['id'] + c.app_version_separator + app_latest_version

        # Save the metadata if it is new
        metadata_path = c.data_path + app_suffix_path + c.app_version_separator + 'metadata.json'
        reviews_path = c.data_path + app_suffix_path + c.app_version_separator + 'reviews.json'
        if(not os.path.exists(metadata_path)):
            c.save(metadata_path, app_metadata)
        
        # Download the APK if it is new
        apk_path = c.apks_path + app_suffix_path + '.apk'
        if(not os.path.exists(apk_path)):
            if(not download_apk(a['id'], apk_path)):
                print('Error while downloading the following app, try to download it manually: ' + a['id'])
                exit()
            elif(not apk_downloader.verify_apk(a['id'], apk_path, app_suffix_path)):
                print('The downloaded APK is not well formed: ' + apk_path)
                exit()
        
        a['latest_crawled_version'] = app_latest_version
        break
    c.save(c.apps_path, apps)

start()


