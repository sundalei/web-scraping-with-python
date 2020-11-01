from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

word_file = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
word_file = BytesIO(word_file)
document = ZipFile(word_file)
xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))