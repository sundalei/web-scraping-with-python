import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def get_page(url):
    req = requests.get(url)
    print(req.text)
    return BeautifulSoup(req.text, 'html.parser')


get_page('https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/')