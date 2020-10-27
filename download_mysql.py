from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Fnst*1234', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES (%s, %s)', (title, content))
    cur.connection.commit()


def get_links(article_url):
    req = Request(article_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'})
    html = urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    articles = bs.find_all('article', {'class': 'post'})
    links = [article.find('a')['href'] for article in articles]
    return links


def get_article(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'})
    html = urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    content_section = bs.find('h4')
    if content_section == None:
        content = title
    else:
        content = content_section.get_text()
    
    print(title, content)
    store(title, content)

links = get_links('http://www.allitebooks.com/')
try:
    for link in links:
        get_article(link)
finally:
    cur.close()
    conn.close()