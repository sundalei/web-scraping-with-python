import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


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


class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
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
        selected_elems = pageObj.select(selector)
        if selected_elems is not None and len(selected_elems) > 0:
            return '\n'.join([elem.get_text() for elem in selected_elems])
        return ''

    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, site.titleTag)
            body = self.safe_get(bs, site.bodyTag)
            print(title)
            print(body)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'div.content span div'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.ArticleBodyWrapper p.Paragraph-paragraph-2Bgue']
]

websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

# crawler.parse(websites[0], 'https://www.oreilly.com/library/view/learning-python-5th/9781449355722/')
crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
# crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
# crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')