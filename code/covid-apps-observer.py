import json
import os
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
        
    # Finally, if everything goes well, save the updated apps.json file with the new timestamps and versions
    c.save(c.APPS_PATH, apps)

def create_report():
    
    apps = json.load(open(c.APPS_PATH, 'r'))

    for a in apps:
        report_creator.create(a)

def main():
    # Argument definition and management
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to the folder containing the JSON file with the apps to analyze', required=True, type=str)
    options = parser.parse_args()
    # We don't even start if the provided path does not exist
    if(os.path.exists(options.input)):
        c.setPaths(options.input)
    else:
        print('Error - the provided path does not exist: ' + options.input)

    collect_data()
    create_report()

    # servers_analyzer.analyze({'id':'it.softmining.projects.covid19.savelifestyle', 'latest_crawled_version': '3.4'})

if __name__ == "__main__":
    main()