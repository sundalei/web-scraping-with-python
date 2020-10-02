from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from scrapetest4 import getInternalLinks, getExternalLinks

# Collects a list of all external URLs found on the site
all_external_links = set()
all_internal_links = set()


def get_all_external_links(site_url):
    html = urlopen(site_url)
    domain = '{}://{}'.format(urlparse(site_url).scheme, urlparse(site_url).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internal_links = getInternalLinks(bs, domain)
    external_links = getExternalLinks(bs, domain)

    for link in external_links:
        if link not in all_external_links:
            all_external_links.add(link)
            print(link)

    for link in internal_links:
        if link not in all_internal_links:
            all_internal_links.add(link)
            get_all_external_links(link)


all_internal_links.add('http://oreilly.com')
get_all_external_links('http://oreilly.com')
