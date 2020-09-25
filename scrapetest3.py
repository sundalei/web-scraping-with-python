from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        _title = bs.body.h1
    except AttributeError:
        return None
    return _title


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img', {'src': re.compile(r'\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])

result = bs.find_all(lambda tag: len(tag.attrs) == 2)
for tag in result:
    print(tag)