from androguard.misc import AnalyzeAPK
from androguard.core.bytecodes.apk import APK
import configuration as c

# Analyses the app with Androguard - https://androguard.readthedocs.io/en/latest/intro/index.html
def analyze(app):
    
    result = {}

    # We open the APK
    apk_path = c.get_apk_path(app)
    a, d, dx = AnalyzeAPK(apk_path)

    # Get all the permissions requested by the app
    requested_permissions = a.get_permissions()

    # Get all the Android activities of the app
    activities = a.get_activities()

    # Get all String constants in the app presumably containing a URL 
    urls = list()
    for u in dx.find_strings("http[s]?://."):
        urls.append(u.get_value())

    # We pack together all the partial results
    result['permissions'] = requested_permissions
    result['activities'] = activities
    result['urls'] = urls
    
    # We save the result into a JSON file
    app_suffix_path = app['id'] + c.SEPARATOR + app['latest_crawled_version']
    result_path = c.DATA_PATH + app_suffix_path + c.SEPARATOR + 'androguard.json' 
    c.save(result_path, result)