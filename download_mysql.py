import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='19880701', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages')
print(cur.fetchall())
cur.close()
conn.close()