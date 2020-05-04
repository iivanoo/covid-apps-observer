import json
from datetime import datetime
import os
import shutil
import re
import configuration as c

# We create the folder containing the report and all its static resources, we return the root folder for this report for convenience
def prepare_folders_structure(app):
    app_suffix_path = app['id'] + c.SEPARATOR + app['latest_crawled_version']
    app_folder_path = c.GLOBAL_PATH + 'reports/resources/' + app_suffix_path + '/'
    
    if os.path.exists(app_folder_path):
        shutil.rmtree(app_folder_path)
    if not os.path.exists(c.GLOBAL_PATH + 'reports/resources/'):
        os.mkdir(c.GLOBAL_PATH + 'reports/resources/')
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
    return (entry is None) or (entry == '') or (entry == 'None')

# Returns the same placeholders dictionary, but it substitues None or other null values with a fixed replacement string
def fill_voids(placeholders):
    replacement = '-'
    for p in placeholders:
        if is_void(placeholders[p]):
            placeholders[p] = replacement
    return placeholders

# Fill the Overview section of the report
def fill_overview(app, metadata, template, report_folder):
    
    icon_path = 'icon.png'
    c.download(metadata['icon'], report_folder + icon_path)

    screenshots = ''
    for i, s in enumerate(metadata['screenshots'], start=1):
        s_path = 'screenshot_' + str(i) + '.png'
        screenshots = screenshots + ' | <img src="' + s_path + '" alt="screenshot" width="300"/> '
        if(i % 3 == 0):
            screenshots = screenshots + ' | \n'  
        c.download(s, report_folder + s_path) 

    placeholders = {
        'ICON_PATH': icon_path,
        'SEPARATOR': c.SEPARATOR,
        'APP_TITLE': metadata['title'],
        'APP_VERSION': app['latest_crawled_version'],
        'APP_ID': app['id'],
        'APP_SUMMARY': metadata['summaryHTML'],
        'APP_PRIVACY_POLICY': metadata['privacyPolicy'],
        'APP_UPDATED': datetime.fromtimestamp(metadata['updated']),
        'APP_RECENT_CHANGES': metadata['recentChangesHTML'],
        'APP_INSTALLS': metadata['installs'],
        'APP_GENRE': metadata['genre'],
        'APP_RELEASE': metadata['released'],
        'APP_SIZE': metadata['size'],
        'APP_ANDROID_VERSION': metadata['androidVersionText'],
        'APP_DESCRIPTION': '> ' + re.sub('[\n|\r]+','\n<br>> ', metadata['description']),
        'SCREENSHOTS': screenshots
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Fill the Development team section of the report
def fill_dev_team(app, metadata, template):
    
    developerWebsite = metadata['developerWebsite']
    if(not is_void(developerWebsite)):
        developerWebsite = '[' + metadata['developerWebsite'] + '](' + metadata['developerWebsite'] + ')'

    developerEmail = metadata['developerEmail']

    developerAddress = metadata['developerAddress']
    if(not is_void(developerAddress)):
        developerAddress = re.sub('[\s|\n|\r]+','%20', developerAddress)
        developerAddress = '[' + metadata['developerAddress'] + '](https://www.google.com/maps/search/' + developerAddress + ') (Google Maps)'

    placeholders = {
        'APP_DEVELOPER': metadata['developer'],
        'DEVELOPER_WEBSITE': developerWebsite,
        'DEV_EMAIL': developerEmail,
        'APP_DEVELOPER_ADDRESS': developerAddress,
        'APP_DEVELOPER_ID': metadata['developerId']
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Given the portion of json file produced by Androwarm, it extracts a more structured and mapped data structure with placeholders 
def get_sdk_info(aw, sdk_info):
    
    result = {
        'target_sdk': None,
        'effective_sdk': None,
        'min_sdk': None,
        'max_sdk': None,
    }

    # We flatten the list into a string so to ease the application of the regexes below
    contents = '\n'.join(aw)

    target_sdk = re.findall(r'Declared target SDK:\s*(\d+)', contents) or None
    effective_sdk = re.findall(r'Effective target SDK:\s*(\d+)', contents) or None
    min_sdk = re.findall(r'Min SDK:\s*(\d+)', contents) or None
    max_sdk = re.findall(r'Max SDK:\s*(\d+)', contents) or None

    # Transform API levels into integers (when possible) so to ease the comparison in the subsequent for iteration 
    if(not target_sdk is None):
        target_sdk = int(target_sdk[0])
    if(not effective_sdk is None):
        effective_sdk = int(effective_sdk[0])
    if(not min_sdk is None):
        min_sdk = int(min_sdk[0])
    if(not max_sdk is None):
        max_sdk = int(max_sdk[0])

    # Iterate over all codenames and when they match we produce the filled string to be put in the report
    for e in sdk_info['codenames']:
        if(e['api_level'] == target_sdk):
            result['target_sdk'] = e['codename'] + ', version ' + e['version'] + ' (API level ' + str(e['api_level']) + ')'
        if(e['api_level'] == effective_sdk):
            result['effective_sdk'] = e['codename'] + ', version ' + e['version'] + ' (API level ' + str(e['api_level']) + ')'
        if(e['api_level'] == min_sdk):
            result['min_sdk'] = e['codename'] + ', version ' + e['version'] + ' (API level ' + str(e['api_level']) + ')'
        if(e['api_level'] == max_sdk):
            result['max_sdk'] = e['codename'] + ', version ' + e['version'] + ' (API level ' + str(e['api_level']) + ')'

    return result

# Fill the Android section of the report
def fill_android(app, androwarn, template):

    sdk_info = json.load(open('static_resources/android_codenames.json', 'r'))

    mapped_info = get_sdk_info(androwarn[3]['androidmanifest.xml'][1][1], sdk_info)

    placeholders = {
        'TARGET_SDK': mapped_info['target_sdk'],
        'EFFECTIVE_SDK': mapped_info['effective_sdk'],
        'MIN_SDK': mapped_info['min_sdk'],
        'MAX_SDK': mapped_info['max_sdk']
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Fill the Permissions section of the report
def fill_permissions(app, androguard, template):
    
    permissions = json.load(open('static_resources/android_permissions.json', 'r'))['permissions']
    permissions_table = ''

    androguard['permissions'].sort()

    for p in androguard['permissions']:
        try:
            description = permissions[p]['description']
            protection_level = permissions[p]['protection_level'].capitalize().replace('|', ' - ')
            if protection_level == 'Dangerous':
                protection_level = '<p class="text-red mb-2">:warning:' + protection_level + '</p>'
        except KeyError:
            description = '-'
            protection_level = '-'
        p = '<br>'.join(p.rsplit('.', 1))
        permissions_table = permissions_table + ' **' + p + '** | ' + protection_level + ' | ' + description + ' \n' 

    placeholders = {
        'PERMISSIONS_TABLE': permissions_table
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Given a country code, we return the Markdown code of the flag of the country
def get_flag(country_code):
    mapping = {
        'US': ':us:',
        'IT': ':it:',
        'CA': ':canada:',
        'ES': ':es:',
        'FR': ':fr:',
        'AR': ':argentina:',
        'AT': ':austria:',
        'BE': ':belgium:',
        'BU': ':bulgaria:',
        'CL': ':chile:',
        'CH': ':china:',
        'CU': ':cuba:',
        'DE': ':de:',
        'FI': ':finland:',
        'CR': ':croatia:',
        'IL': ':israel:',
        'IN': ':india:',
        'IS': ':iceland:',
        'NO': ':norway:',
        'NZ': ':new_zealand:',
        'PO': ':poland:',
        'RO': ':romania:',
        'RU': ':ru:',
        'SE': ':sweden:',
        'UA': ':ukraine:',
        'AU': ':australia:',
        'BR': ':brazil:',
        'CH': ':switzerland:',
        'CZ': ':czech_republic:',
        'DN': ':denmark:',
        'UK': ':uk:',
        'GR': ':greece:',
        'JP': ':jp:',
        'NL': ':netherlands:',
        'PT': ':portugal:',
        'SM': ':san_marino:',
        'TR': ':tr:',
        'VE': ':venezuela:',
        'ZA': ':south_africa:',
    }
    if(country_code in mapping):
        return mapping[country_code] + ' '
    return ''

# Fill the Servers section of the report
def fill_servers(app, servers, template):

    servers_table = ''

    for s in servers:
        if s['registrant'] is None or s['registrant'] == '':
            s['registrant'] = '-'
        if s['registrant_country'] is None or s['registrant_country'] == '':
            s['registrant_country'] = '-'
        if s['creation_date'] is None or s['creation_date'] == '':
            s['creation_date'] = '-'

        servers_table = servers_table + ' | ' + s['name'] + ' | ' + s['registrant'] + ' | ' + get_flag(s['registrant_country']) + s['registrant_country'] + ' | ' + s['creation_date'] + ' |\n' 

    placeholders = {
        'SERVERS_TABLE': servers_table
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Fill the Security Analysis section of the report
def fill_security_analysis(app, androwarn, template):

    security_analysis = androwarn[1]['analysis_results']

    warnings = ''
    
    for e in security_analysis:
        # We ignore the device_settings_harvesting results of Androwarm since it is too verbose and not informative for this project
        if e[0] != 'device_settings_harvesting' and len(e[1]) != 0:
            warnings = warnings + '**' + e[0].capitalize().replace('_', ' ') + '**\n'
            warnings = warnings
            for i, w in enumerate(e[1]):
                warnings = warnings + '> ' + w + '<br>\n'
            warnings = warnings + '\n'
        
    placeholders = {
        'ANDROWARN_RESULTS': warnings,
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Fill the Ratings and Reviews section of the report
def fill_reviews(app, metadata, reviews, template):
    filled_template = template

    return filled_template

# Creates the report about the app
def create(app):

    print('Generating report for: ' + app['id'])

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