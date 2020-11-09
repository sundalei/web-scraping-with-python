import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Fnst*1234', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def getUrl(pageId):
    cur.execute('SELECT url FROM pages WHERE id = %s', (int(pageId)))
    return cur.fetchone()[0]

def getLinks(fromPageId):
    cur.execute('select toPageId from links where fromPageId = %s', (int(fromPageId)))
    if cur.rowcount == 0:
        return []
    return [x[0] for x in cur.fetchall()]

def searchBreadth(targetPageId, paths=[[1]]):
    newPaths = []
    for path in paths:
        links = getLinks(path[-1])
        for link in links:
            if link == targetPageId:
                return path + [link]
            else:
                newPaths.append(path + [link])
    return searchBreadth(targetPageId, newPaths)

nodes = getLinks(1)
targetPageId = 31035
pageIds = searchBreadth(targetPageId)
for pageId in pageIds:
    print(getUrl(pageId))

cur.close()
conn.close()