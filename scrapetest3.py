from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        _title = bs.body.h1
    except AttributeError as e:
        return None
    return _title


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

img = bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
print(img)