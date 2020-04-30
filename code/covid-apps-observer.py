import json
import crawler as crawler
import configuration as c

def start():

    apps = json.load(open(c.apps_path, 'r'))

    for a in apps:
        crawler.crawl_data(a)
    c.save(c.apps_path, apps)

start()
