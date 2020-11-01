from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

word_file = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
word_file = BytesIO(word_file)
document = ZipFile(word_file)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))

word_obj = BeautifulSoup(xml_content.decode('utf-8'), 'xml')
text_strings = word_obj.find_all('w:t')

for text_elem in text_strings:
    style = text_elem.parent.parent.find('w:pStyle')
    if style is not None and style['w:val'] == 'Title':
        print('Title is: {}'.format(text_elem.text))
    else:
        print(text_elem.text)