from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))
        print('-------------------------------------')


class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, target_pattern, absolute_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.target_pattern = target_pattern
        self.absolute_url = absolute_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []
    
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
        selected_elems = page_obj.select(selector)
        if selected_elems is not None and len(selected_elems) > 0:
            return '\n'.join([elem.get_text() for elem in selected_elems])
        return ''

    def parse(self, url):
        """
        Extract content from a given page URL
        """
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, self.site.title_tag)
            body = self.safe_get(bs, self.site.body_tag)
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

    def crawl(self):
        """
        Get pages from website home page
        """
        bs = self.get_page(self.site.url)
        target_pages = bs.find_all('a', rel=re.compile(self.site.target_pattern))
        for target_page in target_pages:
            target_page = target_page.attrs['href']
            if target_page not in self.visited:
                self.visited.append(target_page)
                if not self.site.absolute_url:
                    target_page = '{}{}'.format(self.site.url, target_page)
                self.parse(target_page)

allitebooks = Website('allitebooks', 'http://www.allitebooks.org/', '^(bookmark)', True, 'h1', 'div.entry-content')
crawler = Crawler(allitebooks)
crawler.crawl()