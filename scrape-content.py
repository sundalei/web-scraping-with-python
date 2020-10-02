import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def get_page(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


print('hello world')