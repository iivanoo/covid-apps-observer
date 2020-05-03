import json
import crawler as crawler
import androguard_androwarn_analyzer
import configuration as c

def start():

    apps = json.load(open(c.APPS_PATH, 'r'))

    for a in apps:
        crawled_new_data = crawler.crawl_data(a)
        if(crawled_new_data):
            androguard_androwarn_analyzer.analyze(a)
        
    # Finally, if everything goes well, save the updated apps.json file with the new timestamps and versions
    c.save(c.APPS_PATH, apps)

start()
