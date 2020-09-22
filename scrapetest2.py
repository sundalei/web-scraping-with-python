from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        return None
    return bs


url = 'http://www.pythonscraping.com/pages/warandpeace.html'
bs = getTitle(url)
if bs == None:
    print('Title could not be found')
else:
    nameList = bs.findAll('span', {'class': 'green'})
    for name in nameList:
        print(name.get_text())
