from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'http://pythonscraping.com'


def get_absolute_url(base_url, source):
    print(base_url)
    print(source)
    return source

html = urlopen('http://www.pythonscraping.com/')
bs = BeautifulSoup(html, 'html.parser')
download_list = bs.find_all(src=True)

for download in download_list:
    file_url = get_absolute_url(base_url, download['src'])