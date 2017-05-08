#coding=utf-8
import method
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

def get_weather(url):
    time = url.split('/')
    time = time[-1]
    time = time.split('&')
    #拆分网址，获取网址中的时间信息
    tmp = []
    for i in time:
        i = filter(str.isdigit,i)
        tmp.append(i)
    #过滤出其中的数字
    time = '/'.join(tmp)
    #把数字信息挑选出来
    page_html = method.get_htmlsoup(url)
    print time
    weatherlist = page_html.find(class_="uk-table uk-table-striped uk-table-hover")
    weatherlist = weatherlist.find_all('tr')
    #获取天气信息
    result = []
    for place in weatherlist:
        attribute = place.find_all('td')
        tmp = [time,'\t']#列表内容用tab分割
        for i in attribute:
            i = (i.get_text()).replace('\n',' ')
            tmp.append((i.strip()).encode('utf-8'))
            tmp.append('\t')
        result.append(tmp) 
        #把天气信息储存成列表，列表第一项为时间       
    return result


fh = open('date.txt','r')
dates = fh.readlines()
date_time = []
for i in dates:
    i = i.strip()
    tmp = i.split('\t')
    date_time.append(tmp)
#读取date文件的内容，把这些内容逐行读取出来储存成列表

count = 0
for date in date_time:
    url = 'http://www.wetterkontor.de/de/wetter/deutschland/monatswerte.asp?y='+date[0]+'&m='+date[1]
    #格式化网页信息
    result = get_weather(url)
    print date

    count = count+1
    tmp = date_time[count:]
    #以下内容用于断点续传
    fh = open('date.txt','w')
    for i in tmp:
        fh.write('\t'.join(i)+'\n')
    #更新日期列表
    fh = open('weather.txt','a')
    for i in result[1:]:
        fh.write(''.join(i)+'\n')
    fh.close()
    #保存程序
