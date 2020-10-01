from urllib.request import urlopen
from urllib.parse import urlparse


# Collects a list of all external URLs found on the site
all_external_links = set()
all_internal_links = set()


def get_all_external_links(site_url):
    html = urlopen(site_url)
    domain = '{}://{}'.format(urlparse(site_url).scheme, urlparse(site_url).netloc)
    print(domain)


all_internal_links.add('http://oreilly.com')
get_all_external_links('http://oreilly.com')