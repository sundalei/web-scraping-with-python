from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def cleanInput(content):
    content = re.sub('\n|[\[\d+\]]', ' ', content)
    content = bytes(content, 'utf-8')
    content = content.decode('ascii', 'ignore')
    return content


def getNgrams(content, n):
    content = cleanInput(content)
    print(content)

# html = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)')
# bs = BeautifulSoup(html, 'html.parser')
# content = bs.find('div', {'id': 'mw-content-text'}).get_text()
content = 'Python features a dynamic type syst[123]em and automatic memory management. It supports multiple programming paradigms...'
ngrams = getNgrams(content, 2)
# print(ngrams)
# print('2-grams count is: ' + str(len(ngrams)))