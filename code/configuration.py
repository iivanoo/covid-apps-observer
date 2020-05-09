import json
import os
import requests

SEPARATOR = '___'

NUM_REVIEWS = 1000


def setPaths(path):

    global GLOBAL_PATH
    global APPS_PATH
    global DATA_PATH
    global APKS_PATH
    global REPORTS_PATH

    if not path.endswith('/'):
        path = path + '/'
    GLOBAL_PATH = path
    APPS_PATH = path + 'apps.json'
    DATA_PATH = GLOBAL_PATH + 'data/'
    APKS_PATH = GLOBAL_PATH + 'apks/'
    REPORTS_PATH = GLOBAL_PATH + 'reports/'

    if not os.path.exists(APPS_PATH):
        os.makedirs(APPS_PATH)
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    if not os.path.exists(APKS_PATH):
        os.makedirs(APKS_PATH)
    if not os.path.exists(REPORTS_PATH):
        os.makedirs(REPORTS_PATH)


# Downloads a remote resource pointed by url into path
def download(url, path):
    img_data = requests.get(url, allow_redirects=True).content
    with open(path, 'wb') as handler:
        handler.write(img_data)


# Save JSON data into the given filePath
def save(file_path, data):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4, default=str)


# Get the complete path of the APK of the app
def get_apk_path(app):
    app_latest_version = app['latest_crawled_version']
    app_suffix_path = app['id'] + SEPARATOR + app_latest_version
    return APKS_PATH + app_suffix_path + '.apk'


# Get the raw data resulting from either a previous analysis or a previous crawl
# analysis_type = androguard | androwarn | metadata | reviews 
def ger_raw_data(app, analysis_type: str):
    app_latest_version = app['latest_crawled_version']
    app_suffix_path = app['id'] + SEPARATOR + app_latest_version
    file_path = DATA_PATH + app_suffix_path + SEPARATOR + analysis_type + '.json'
    return json.load(open(file_path, 'r'))
