import json

DATA_PATH = './data/'
APKS_PATH = './apks/'

APPS_PATH = DATA_PATH + 'apps.json'

SEPARATOR = '___'

NUM_REVIEWS = 1000

# Save JSON data into the given filePath
def save(filePath, data):
    with open(filePath, 'w') as outfile:  
        json.dump(data, outfile, indent=4, default=str)

# Get the complete path of the APK of the app
def get_apk_path(app):
    app_latest_version = app['latest_crawled_version']
    app_suffix_path = app['id'] + SEPARATOR + app_latest_version
    return APKS_PATH + app_suffix_path + '.apk'