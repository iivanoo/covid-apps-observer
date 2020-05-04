import time
import json
import sys
import os
import time
from google_play_scraper import app, Sort, reviews
import ssl
import random
import configuration as c
import apk_downloader

def download_apk(app_to_download, apk_path):
    print('Downloading the APK of: ' + app_to_download)
    return apk_downloader.download_apk(app_to_download, apk_path)
    

def get_gp_metadata(app_to_scrape):
    app_metadata = app(app_to_scrape['id'], lang=app_to_scrape['store_lang'], country=app_to_scrape['store_country'])
    return app_metadata

def get_reviews(app_to_scrape):
    time.sleep(random.randrange(10))
    print("Downloading reviews for: " + app_to_scrape['id'])
    
    result, continuation_token = reviews(
    app_to_scrape['id'],
    lang=app_to_scrape['store_lang'],
    country=app_to_scrape['store_country'],
    sort=Sort.NEWEST, 
    count=c.NUM_REVIEWS)

    return result

def crawl_data(app):

    # Tells to the caller that we just downloaded new data
    is_new_data_available = False

    # Download Google Play metadata
    app_metadata = get_gp_metadata(app)
    app_latest_version = app_metadata['version']
    app_suffix_path = app['id'] + c.SEPARATOR + app_latest_version

    # Save the metadata if it is new
    metadata_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'metadata.json'
    if(not os.path.exists(metadata_path)):
        is_new_data_available = True
        c.save(metadata_path, app_metadata)

    # Save the reviews if they are about an older version of the app 
    reviews_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'reviews.json'
    if(not os.path.exists(reviews_path)):
        app_reviews = get_reviews(app)
        c.save(reviews_path, app_reviews)
    
    # Download the APK if it is new
    apk_path = c.APKS_PATH + app_suffix_path + '.apk'
    if(not os.path.exists(apk_path)):
        if(not download_apk(app['id'], apk_path)):
            print('Error while downloading the following app, try to download it manually: ' + app['id'])
            exit()
        elif(not apk_downloader.verify_apk(app['id'], apk_path, app_suffix_path)):
            print('The downloaded APK is not well formed: ' + apk_path)
            exit()
    
    app['latest_crawled_version'] = app_latest_version
    app['latest_crawl'] = int(time.time())
    
    # Let's inform the user about whether new data has been crawled
    if(is_new_data_available):
        print('Crawled new data for: ' + app['id'] +  ' - version: ' + app_latest_version)
    else:
        print('Already up to date: ' + app['id'] +  ' - version: ' + app_latest_version)

    return is_new_data_available