import json

DATA_PATH = './data/'
APKS_PATH = './apks/'

APPS_PATH = DATA_PATH + 'apps.json'

SEPARATOR = '___'

NUM_REVIEWS = 1000

def save(filePath, data):
    with open(filePath, 'w') as outfile:  
        json.dump(data, outfile, indent=4, default=str)