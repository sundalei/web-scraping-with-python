from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.error import HTTPError
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
    def __init__(self, name, url, search_url, result_listing, result_url, absolute_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.search_url = search_url
        self.result_listing = result_listing
        self.result_url = result_url
        self.absolute_url = absolute_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    def get_page(self, url):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'})
            html = urlopen(req)
        except URLError:
            return None
        except HTTPError:
            return None
        return BeautifulSoup(html.read(), 'html.parser')


    def safe_get(self, page_obj, selector):
        """
        Utility function used to get a content string from a 
        Beautiful Soup object and a selector. Returns an empty 
        string if no object is found for the given selector
        """
        children = page_obj.select(selector)
        if children is not None and len(children) > 0:
            return children[0].get_text()
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
        bs = self.get_page(site.search_url + topic)
        search_results = bs.select(site.result_listing)
        for result in search_results:
            url = result.select(site.result_url)[0].attrs['href']
            # Check to see whether it's a relative or an absolute URL
            if (site.absolute_url):
                bs = self.get_page(url)
            else:
                bs = self.get_page(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URL. Skipping!')
                return
            title = self.safe_get(bs, site.title_tag)
            body = self.safe_get(bs, site.body_tag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    ['allitebooks', 'http://www.allitebooks.org/', 'http://www.allitebooks.org/?s=', 'article.post', 'article.post a', True, 'h1', 'div.entry-content']
    #['allitebooks', 'https://www.allitebooks.in/', 'https://www.allitebooks.in/?s=', 'div.td-module-meta-info', 'a', True, 'h1', 'div.entry-content']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

topics = ['docker']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for site in sites:
        crawler.search(topic, site)