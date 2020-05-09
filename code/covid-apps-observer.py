import json
import os
import ssl
import argparse
import crawler as crawler
import androguard_androwarn_analyzer
import servers_analyzer
import report_creator
import configuration as c

def collect_data():

    apps = json.load(open(c.APPS_PATH, 'r'))

    for a in apps:
        # Crawl data from the Google Play store
        crawled_new_data = crawler.crawl_data(a)

        # if the app has a new release we did not analyze before...
        if(crawled_new_data):
            # Launch the Androguard and Androwarn analyses
            androguard_androwarn_analyzer.analyze(a)
            # Analyze the servers pointed by the URLs we found in the String analysis of Androguard
            servers_analyzer.analyze(a)
        
    # Finally, if everything goes well, save the updated apps.json file with the new timestamps and versions
    c.save(c.APPS_PATH, apps)

def create_report(author_name, author_email, report_title):
    
    apps = json.load(open(c.APPS_PATH, 'r'))

    app_reports = {}
    
    # We firstly create the internal reports, one for each analyzed app (and we accumulate of their contents)
    for a in apps:
        app_reports[a['id'] + c.SEPARATOR + a['latest_crawled_version']] = report_creator.create(a)
    
    # We create the final gloabl report, which will also include each single app report
    global_report_path = report_creator.create_global_report(apps, app_reports, author_name, author_email, report_title)

    print('Congratulations, the analysis is over! The global report is available here: ' + global_report_path)

# We run the full analysis on the apps.json file provided as input
def run_analysis(input, author_name, author_email, report_title):
    
    # We don't even start if the provided path does not exist
    if(os.path.exists(options.input)):
        c.setPaths(options.input)
    else:
        print('Error - the provided path does not exist: ' + options.input)
        exit()

    collect_data()
    create_report(author_name, author_email, report_title)

def main():
    # Arguments definition and management
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to the folder containing the JSON file with the apps to analyze', required=True, type=str)
    parser.add_argument('-an', '--author_name', help='Name of the author of the analysis', required=False, type=str)
    parser.add_argument('-ae', '--author_email', help='Email address of the author of the analysis', required=False, type=str)
    parser.add_argument('-rt', '--report_title', help='Title of the report to be generated', required=False, type=str)
    options = parser.parse_args()

    # This will allow us to trust SSL certificates from the servers we will interact with (e.g., the one for downloading NLTK stop word)
    ssl._create_default_https_context = ssl._create_unverified_context

    run_analysis(options.input, options.author_name, options.author_email, options.report_title)

if __name__ == "__main__":
    main()