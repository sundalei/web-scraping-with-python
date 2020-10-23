import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

download_directory = 'downloaded'
base_url = 'http://pythonscraping.com'


def get_absolute_url(base_url, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('https://www.'):
        url = 'https://{}'.format(source[12:])
    elif source.startswith('http://'):
        url = source
    elif source.startswith('https://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    else:
        url = '{}/{}'.format(base_url, source)
    
    if base_url not in url:
        return None
    return url


def get_download_path(base_url, absolute_url, download_directory):
    path = absolute_url.replace('www.', '')
    path = path.replace(base_url, '')
    index = path.find('?')
    if index > 0:
        path = path.replace(path[index:], '')
    path = download_directory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


html = urlopen('http://www.pythonscraping.com/')
bs = BeautifulSoup(html, 'html.parser')
download_list = bs.find_all(src=True)

for download in download_list:
    file_url = get_absolute_url(base_url, download['src'])
    if file_url is not None:
        print(file_url)
        urlretrieve(file_url, get_download_path(base_url, file_url, download_directory))