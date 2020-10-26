from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='19880701', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title, content))
    cur.connection.commit()


def get_links(article_url):
    html = urlopen('http://en.wikipedia.org' + article_url)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id': 'mw-content-text'}).find_all('p').get_text()
    print(content)


links = get_links('/wiki/Kevin_Bacon')

# cur.execute('SELECT * FROM pages')
# print(cur.fetchall())
# cur.close()
# conn.close()