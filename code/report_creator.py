import json
from datetime import datetime
import os
import shutil
import re
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import nltk
from datetime import datetime
import pycountry
from nltk.corpus import stopwords
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
def fill_voids(placeholders, replacement='-'):
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
        screenshots = screenshots + ' | <img src="<<<REBASE_ME>>>' + s_path + '" alt="screenshot" width="300"/> '
        if(i % 3 == 0):
            screenshots = screenshots + ' | \n'  
        c.download(s, report_folder + s_path) 

    placeholders = {
        'ICON_PATH': '<<<REBASE_ME>>>' + icon_path,
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
        'APP_DESCRIPTION': '> ' + re.sub('[\n|\r]+','\n<br>', metadata['description']),
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
                protection_level = ':warning:**' + protection_level + '**'
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
                warnings = warnings + '> - ' + w + '<br>\n'
            warnings = warnings + '\n'
        
    placeholders = {
        'ANDROWARN_RESULTS': warnings,
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Fill the Ratings section of the report
def fill_ratings(app, metadata, template):
    placeholders = {
        'APP_TITLE': metadata['title'],
        'APP_MIN_INSTALLS': metadata['minInstalls'],
        'APP_RATINGS': metadata['ratings'],
        'APP_SCORE': metadata['score'],
        'APP_5_STARS': metadata['histogram'][4],
        'APP_4_STARS': metadata['histogram'][3],
        'APP_3_STARS': metadata['histogram'][2],
        'APP_2_STARS': metadata['histogram'][1],
        'APP_1_STAR': metadata['histogram'][0]
    }

    placeholders = fill_voids(placeholders)
    return fill_placeholders(placeholders, template)

# Retrieves the latest "amount" reviews of "stars" stars from "reviews"
def get_reviews(stars, amount, reviews):
    result = ''
    count = 0
    i = 0
    while count != amount and i < len(reviews):
        if(reviews[i]['score'] == stars):
            count = count + 1
            result = result + '> ' + reviews[i]['content'].replace('**', '\*\*') + '<br> :date: __' + reviews[i]['at'] + '__\n\n'
        i = i + 1
    if count == 0:
        result = 'No recent reviews available with ' + str(stars) + ' stars.'
    return result

# Generates a word cloud of the most used terms in the reviews with "stars" stars
def generate_word_cloud(stars, reviews, app, report_folder):
    count = 0
    text_to_plot = ''
    # We concatenate all the reviews with the same number of stars into a single string 
    for r in reviews:
        if(r['score'] == stars):
            count = count + 1
            text_to_plot = text_to_plot + ' ' + r['content']

    if count > 0:
        # We remove all stop words from the collected reviews
        nltk.download('stopwords')
        # We split the string so to be able to remove stop words
        word_list = text_to_plot.split( )
        # Stop words depend on the language of the Google Play store from which we are crawling
        language = pycountry.languages.get(alpha_2=app['store_lang']).name.lower()
        filtered_words = [word for word in word_list if word not in stopwords.words(language)]
        # We join back the string
        text_to_plot = ' '.join(filtered_words)

        # We generate the word cloud
        wc = WordCloud(width=600, height=300, background_color="white")
        wc.generate(text_to_plot)

        file_path = str(stars) + '_star_reviews_wordcloud.png'
        wc.to_file(report_folder + file_path)

        return '<img src="<<<REBASE_ME>>>' + file_path + '" alt="' + app['id'] + ' ' + str(stars) + ' reviews"/>'
    return None

# Fill the Reviews section of the report
def fill_reviews(app, metadata, reviews, template, report_folder):
    placeholders = {
        '5_STAR_WORDCLOUD': generate_word_cloud(5, reviews, app, report_folder),
        '4_STAR_WORDCLOUD': generate_word_cloud(4, reviews, app, report_folder),
        '3_STAR_WORDCLOUD': generate_word_cloud(3, reviews, app, report_folder),
        '2_STAR_WORDCLOUD': generate_word_cloud(2, reviews, app, report_folder),
        '1_STAR_WORDCLOUD': generate_word_cloud(1, reviews, app, report_folder),
        '5_STAR_REVIEWS': get_reviews(5, 10, reviews),
        '4_STAR_REVIEWS': get_reviews(4, 10, reviews),
        '3_STAR_REVIEWS': get_reviews(3, 10, reviews),
        '2_STAR_REVIEWS': get_reviews(2, 10, reviews),
        '1_STAR_REVIEWS': get_reviews(1, 10, reviews),
    }

    placeholders = fill_voids(placeholders, '')
    return fill_placeholders(placeholders, template)

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

        # Fill the Ratings section
        template = fill_ratings(app, metadata, template)

        # FIll the Reviews section
        template = fill_reviews(app, metadata, reviews, template, report_folder)

        with open(report_folder + 'report.md', "w") as report_file:
            report_file.write(template.replace('<<<REBASE_ME>>>', ''))
        return template
    return ''

# Iterates over all analyzed apps and generates their corresponding portion of TOC
def generate_apps_toc(apps):
    result = ''

    for a in apps:
        app_name = c.ger_raw_data(a, 'metadata')['title']
        app_handle = re.sub(r"[,:;@#?!&$]+", '', app_name).strip().lower().replace(' ', '-')
        result = result + '- [' + app_name + '](#' + app_handle + ')\n' 

    return result

# Generates the summary table at the beginning of the global report
def get_analysed_apps(apps):
    result = ''

    for a in apps:
        app_data = c.ger_raw_data(a, 'metadata')
        app_name = app_data['title']
        app_icon_path = 'resources/' + a['id'] + c.SEPARATOR + a['latest_crawled_version'] + '/icon.png'
        result = result + '| <img src="' + app_icon_path + '" alt="' + app_name + ' icon" width="40"/> | ' + app_name + '\n' 

    return result

# Creates the report about the app
def create_global_report(apps, app_reports, author_name, author_email, report_title):

    print('Generating the global report...')

    with open('./report_templates/global_template.md', 'r') as template_file:
        template = template_file.read()

        # Timestamp used in the header of the report and in the name of the file
        now = datetime.now()
        timestamp = str(now.year) + '_' + str(now.month) + '_' + str(now.day)

        # We rebase the paths to the images in the apps' reports so that they can still be used in the global report
        rebased_app_reports = ''
        for k, r in app_reports.items():
            new_base = 'resources/' + k + '/'
            rebased_report = r.replace('<<<REBASE_ME>>>', new_base)
            rebased_app_reports = rebased_app_reports + rebased_report + '\n'

        # We fetch the contents of the requirements.txt file so to include them in the credits at the end of the report
        with open('requirements.txt', 'r') as req_file:
            requirements_contents = req_file.read()
            requirements_contents = '- ' + requirements_contents.replace('\n', '\n- ')[:-2]

            if(report_title is None):
                report_title = 'COVID-related Android apps report'

            placeholders = {
                'REPORT_TITLE': report_title,
                'AUTHOR_NAME': author_name,
                'AUTHOR_EMAIL': author_email,
                'CREATED_AT': timestamp.replace('_', '/'),
                'TOC': generate_apps_toc(apps),
                'APPS_REPORTS': rebased_app_reports,
                'REQUIREMENTS_CONTENTS': requirements_contents,
                'ANALYSED_APPS': get_analysed_apps(apps)
            }

            placeholders = fill_voids(placeholders)
            filled_template = fill_placeholders(placeholders, template)

            file_path = c.REPORTS_PATH + 'report_' + timestamp + '.md'
            with open(file_path, "w") as report_file:
                report_file.write(filled_template)
        
            return file_path
