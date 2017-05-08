#coding=utf-8
import method
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

def get_weather(url):
    time = url.split('/')
    time = time[-1]
    time = time.split('&')
    tmp = []
    for i in time:
        i = filter(str.isdigit,i)
        tmp.append(i)
    time = '/'.join(tmp)
    page_html = method.get_htmlsoup(url)
    print time
    weatherlist = page_html.find(class_="uk-table uk-table-striped uk-table-hover")
    weatherlist = weatherlist.find_all('tr')
    result = []
    for place in weatherlist:
        attribute = place.find_all('td')
        tmp = [time,'\t']
        for i in attribute:
            i = (i.get_text()).replace('\n',' ')
            tmp.append((i.strip()).encode('utf-8'))
            tmp.append('\t')
        result.append(tmp)        
    return result

fh = open('date.txt','r')
dates = fh.readlines()
date_time = []
for i in dates:
    i = i.strip()
    tmp = i.split('\t')
    date_time.append(tmp)

count = 0
for date in date_time:
    url = 'http://www.wetterkontor.de/de/wetter/deutschland/monatswerte.asp?y='+date[0]+'&m='+date[1]
    result = get_weather(url)
    print date
    count = count+1
    tmp = date_time[count:]
    fh = open('date.txt','w')
    for i in tmp:
        fh.write('\t'.join(i)+'\n')
    fh = open('weather.txt','a')
    for i in result[1:]:
        fh.write(''.join(i)+'\n')
    fh.close()
