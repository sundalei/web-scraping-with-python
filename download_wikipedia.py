from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from random import shuffle

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Fnst*1234', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')


def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def load_pages():
    cur.execute('SELECT * FROM pages')
    pages = [row[1] for row in cur.fetchall()]
    return pages


def insert_link(from_page_id, to_page_id):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', (int(from_page_id), int(to_page_id)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', (int(from_page_id), int(to_page_id)))
        conn.commit()


def get_links(page_url, recursion_level, pages):
    if recursion_level > 4:
        return
    
    page_id = insertPageIfNotExists(page_url)
    html = urlopen('http://en.wikipedia.org{}'.format(page_url))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]

    for link in links:
        insert_link(page_id, insertPageIfNotExists(link))
        if link not in pages:
            print(link)
            # We have encountered a new page, add it and search it for links
            pages.append(link)
            get_links(link, recursion_level + 1, pages)


get_links('/wiki/Kevin_Bacon', 0, load_pages())

cur.close()
conn.close()