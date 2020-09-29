from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl +').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingSite):
    html = urlopen(startingSite)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingSite).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
    else:
        return externalLinks


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print(externalLink)


followExternalOnly('https://oreilly.com/')