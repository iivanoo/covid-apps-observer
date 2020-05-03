import lib.whois as whois

# Polishes the list of URLs used in the app and performs a whois lookup on the most promising ones
def analyze(app):
    # TODO complete this analysis
    domain = whois.query('www.google.com')
    print(domain.__dict__)