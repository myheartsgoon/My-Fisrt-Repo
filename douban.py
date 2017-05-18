import requests
from bs4 import BeautifulSoup
import time

start = time.time()
count = 1
urllist = ['https://movie.douban.com/top250']

def getres(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return BeautifulSoup(res.text, 'html.parser')

def getelement(soup):
    for movie in soup.select('.item'):
        global count
        title = movie.select('.title')[0].text
        rate = movie.select('.rating_num')[0].text
        year = movie.select('.bd p br')[0].text.split('/')[0].strip()
        print(count, title, rate, year)
        count += 1

def getallurl():
    soup = getres(urllist[0])
    newurl = soup.select('.paginator')[0].select('a')
    for a in newurl:
        url = urllist[0] + a['href']
        if url not in urllist:
            urllist.append(url)

getallurl()
for url in urllist:
    soup = getres(url)
    getelement(soup)

stop = time.time()
print('\n', stop-start)