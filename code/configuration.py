import json

data_path = './data/'
apks_path = './apks/'

apps_path = data_path + 'apps.json'

app_version_separator = '___'

def save(filePath, data):
    with open(filePath, 'w') as outfile:  
        json.dump(data, outfile, indent=4)