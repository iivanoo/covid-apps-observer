import json
import crawler as crawler
import configuration as c

def start():

    apps = json.load(open(c.APPS_PATH, 'r'))

    for a in apps:
        crawler.crawl_data(a)

    # Finally, if everything goes well, save the updated apps.json file with the new timestamps and versions
    c.save(c.APPS_PATH, apps)

start()
