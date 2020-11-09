import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Fnst*1234', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def getLinks(fromPageId):
    pass

nodes = getLinks(1)


cur.close()
conn.close()