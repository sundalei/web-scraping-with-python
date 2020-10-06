import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print('New article found for topic: {}'.format(self.topic))
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))
        print('-------------------------------------')


class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def get_page(self, url):
        try:
            req = requests.get(url)
        except RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')


    def safe_get(self, pageObj, selector):
        """
        Utility function used to get a content string from a 
        Beautiful Soup object and a selector. Returns an empty 
        string if no object is found for the given selector
        """
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, site.titleTag)
            body = self.safe_get(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.get_page(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            # Check to see whether it's a relative or an absolute URL
            if (site.absoluteUrl):
                bs = self.get_page(url)
            else:
                bs = self.get_page(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URL. Skipping!')
                return
            title = self.safe_get(bs, site.titleTag)
            body = self.safe_get(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    ['allitebooks', 'http://www.allitebooks.org/', 'http://www.allitebooks.org/?s=', 'article.post', 'article.post a', True, 'h1', 'div.entry-content']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

topics = ['docker']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for site in sites:
        crawler.search(topic, site)