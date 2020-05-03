import json

DATA_PATH = '../data/'
APKS_PATH = '../apks/'

APPS_PATH = '../apps.json'

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

# Get the raw data resulting from either a previous analysis or a previous crawl
# analysis_type = androguard | androwarn | metadata | reviews 
def ger_raw_data(app, analysis_type: str):
    app_latest_version = app['latest_crawled_version']
    app_suffix_path = app['id'] + SEPARATOR + app_latest_version
    file_path = DATA_PATH + app_suffix_path + SEPARATOR + analysis_type + '.json'
    return json.load(open(file_path, 'r'))