import json
from datetime import datetime
import os
import shutil
import configuration as c

# We create the folder containing the report and all its static resources, we return the root folder for this report for convenience
def prepare_folders_structure(app):
    app_suffix_path = app['id'] + c.SEPARATOR + app['latest_crawled_version']
    app_folder_path = c.GLOBAL_PATH + 'reports/resources/' + app_suffix_path + '/'
    
    if os.path.exists(app_folder_path):
        shutil.rmtree(app_folder_path)
    os.mkdir(app_folder_path)

    return app_folder_path

# Loads all the json files one by one containing the data which will populate the report
def load_data(app):
    app_suffix_path = app['id'] + c.SEPARATOR + app['latest_crawled_version']

    metadata_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'metadata.json'
    metadata = json.load(open(metadata_path, 'r'))
    
    reviews_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'reviews.json'
    reviews = json.load(open(reviews_path, 'r'))

    servers_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'servers.json'
    servers = json.load(open(servers_path, 'r'))

    androguard_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'androguard.json'
    androguard = json.load(open(androguard_path, 'r'))

    androwarn_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'androwarn.json'
    androwarn = json.load(open(androwarn_path, 'r'))

    return metadata, reviews, servers, androguard, androwarn

# Iterates over all entries of placeholders and replaces every key within placeholders into its corresponding value
def fill_placeholders(placeholders, template):
    filled_template = template
    for key in placeholders:
        filled_template = filled_template.replace('<<<' + key + '>>>', str(placeholders[key]))
    return filled_template

# Checks if the passed value is usable in the produced report (e.g., if it is not None)
def is_void(entry):
    return (entry is None) or (entry == '')

# Returns the same placeholders dictionary, but it substitues None or other null values with a fixed replacement string
def fill_voids(placeholders):
    replacement = '-'
    for p in placeholders:
        if is_void(placeholders[p]):
            placeholders[p] = replacement
    return placeholders

# Fill the Overview section of the report
def fill_overview(app, metadata, template, report_folder):
    
    icon_path = report_folder + 'icon.png'
    c.download(metadata['icon'], icon_path)

    screenshots = ''
    for i, s in enumerate(metadata['screenshots'], start=1):
        s_path = report_folder + 'screenshot_' + str(i) + '.png'
        screenshots = screenshots + '<img src="' + s_path + '" alt="screenshot" width="300"/>\n'  
        c.download(s, s_path) 

    placeholders = {
        'ICON_PATH': icon_path,
        'SEPARATOR': c.SEPARATOR,
        'APP_TITLE': metadata['title'],
        'APP_VERSION': app['latest_crawled_version'],
        'APP_ID': app['id'],
        'APP_SUMMARY': metadata['summary'],
        'APP_PRIVACY_POLICY': metadata['privacyPolicy'],
        'APP_UPDATED': datetime.fromtimestamp(metadata['updated']),
        'APP_RECENT_CHANGES': metadata['recentChanges'],
        'APP_INSTALLS': metadata['installs'],
        'APP_GENRE': metadata['genre'],
        'APP_RELEASE': metadata['released'],
        'APP_SIZE': metadata['size'],
        'APP_ANDROID_VERSION': metadata['androidVersionText'],
        'APP_DESCRIPTION': metadata['description'],
        'SCREENSHOTS': screenshots
    }

    placeholders = fill_voids(placeholders)
    
    return fill_placeholders(placeholders, template)

# Fill the Development team section of the report
def fill_dev_team(app, metadata, template):
    
    developerWebsite = metadata['developerWebsite']
    if(not is_void(developerWebsite)):
        developerWebsite = '[' + metadata['developerWebsite'] + '][' + metadata['developerWebsite'] + ']'

    developerEmail = metadata['developerEmail']
    if(not is_void(developerEmail)):
        developerEmail = '[mailto:' + metadata['developerEmail'] + '][' + metadata['developerEmail'] + ']'

    developerAddress = metadata['developerAddress']
    if(not is_void(developerAddress)):
        developersAddress = '[' + metadata['developerAddress'] + '][https://www.google.com/maps/search/' + metadata['developerAddress'] + '/] (Google Maps)'

    placeholders = {
        'APP_DEVELOPER': metadata['developer'],
        'DEVELOPER_WEBSITE': developerWebsite,
        'DEV_EMAIL': developerEmail,
        'APP_DEVELOPER_ADDRESS': developerAddress,
        'APP_DEVELOPER_ID': metadata['developerId']
    }

    placeholders = fill_voids(placeholders)
    
    return fill_placeholders(placeholders, template)

# Fill the Android section of the report
def fill_android(app, androwarn, template):
    placeholders = {
        # 'TARGET_SDK_CODENAME': '',
        # 'TARGET_SDK_VERSION': androwarn['developerWebsite'],
        # 'EFFECTIVE_SDK_CODENAME': '',
        # 'EFFECTIVE_SDK_VERSION': androwarn['developerAddress'],
        # 'MIN_SDK_CODENAME': '',
        # 'MIN_SDK_VERSION': androwarn['developerId'],
        # 'MAX_SDK_CODENAME': '',
        # 'MAX_SDK_VERSION': androwarn['developerId']
    }
    
    return fill_placeholders(placeholders, template)

# Fill the Permissions section of the report
def fill_permissions(app, androguard, template):
    filled_template = template

    return filled_template

# Fill the Servers section of the report
def fill_servers(app, servers, template):
    filled_template = template

    return filled_template

# Fill the Security Analysis section of the report
def fill_security_analysis(app, androwarn, template):
    filled_template = template

    return filled_template

# Fill the Ratings and Reviews section of the report
def fill_reviews(app, metadata, reviews, template):
    filled_template = template

    return filled_template

# Creates the report about the app
def create(app):

    report_folder = prepare_folders_structure(app)

    with open('./report_templates/app_template.md', 'r') as template_file:
        template = template_file.read()

        # We fetch all data from the json files
        metadata, reviews, servers, androguard, androwarn = load_data(app)

        # Fill the Overview section
        template = fill_overview(app, metadata, template, report_folder)

        # Fill the Development team section
        template = fill_dev_team(app, metadata, template)

        # Fill the Android section
        template = fill_android(app, androwarn, template)

        # Fill the Permissions section
        template = fill_permissions(app, androguard, template)

        # Fill the Servers section
        template = fill_servers(app, servers, template)

        # Fill the Security Analysis section
        template = fill_security_analysis(app, androwarn, template)

        # Fill the Ratings and Reviews section
        template = fill_reviews(app, metadata, reviews, template)

        with open(report_folder + 'report.md', "w") as report_file:
            report_file.write(template)
        return template
    return ''