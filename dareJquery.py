# -*- coding: UTF-8 -*-
import cookielib
import json
import string
import urllib2
import urllib
from emailSystem import sendEmail

import sys

import time
from bs4 import BeautifulSoup

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


BASIC_URL = "http://202.120.165.79:8800/Default.aspx"
QUERY_URL1 = "http://202.120.165.79:8801/Default.aspx"
QUERY_URL2 = "http://202.120.165.79:8802/Default.aspx"
INPOS_URL = ""  # 自行添加用户json文件地址


queryData1={
    '__VIEWSTATE':'',
    '__VIEWSTATEGENERATOR':'',
    'btnone':''
}

queryData2={
    '__VIEWSTATE':'',
    '__VIEWSTATEGENERATOR':'',
    'btntwo':''
}


def start(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host':'nyglzx.tongji.edu.cn'
}):
    cj = cookielib.CookieJar()
    pro = urllib2.HTTPCookieProcessor(cj)

    opener = urllib2.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def main():
    opener = start()
    try:
        data = opener.open(BASIC_URL, timeout=5000).read()
        soup = BeautifulSoup(data, 'html.parser')
        queryData1['__VIEWSTATE'] = soup.find(id="__VIEWSTATE")['value']
        queryData1['__VIEWSTATEGENERATOR'] = soup.find(id="__VIEWSTATEGENERATOR")['value']
        queryData1['btnone'] = soup.find(id='btnone')['value']

        queryData2['__VIEWSTATE'] = soup.find(id="__VIEWSTATE")['value']
        queryData2['__VIEWSTATEGENERATOR'] = soup.find(id="__VIEWSTATEGENERATOR")['value']
        queryData2['btntwo'] = soup.find(id='btntwo')['value']

        with open(INPOS_URL, 'r') as f:
            information = json.load(f)
            f.close()

        for member in information:
            finalData={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            '__VIEWSTATE':'',
            '__VIEWSTATEGENERATOR':'',
            'drlouming':'',
            'drceng':'',
            'radio':'usedR',
            'ImageButton1.x':'50',
            'ImageButton1.y':'50'
            }
            if member['port'] =='2':
                request = urllib2.Request(BASIC_URL, urllib.urlencode(queryData2).encode())
                data = opener.open(request, timeout=10000).read()
                soup = BeautifulSoup(data, 'html.parser')
                finalData['drlouming'] = member['drlouming']
                finalData['drceng'] = member['drceng']
                finalData['DropDownList1'] = member['DropDownList1']
                finalData['txt_fangjian'] = member['txt_fangjian']
                QUERY_URL = QUERY_URL1
            else:
                request = urllib2.Request(BASIC_URL, urllib.urlencode(queryData1).encode())
                data = opener.open(request, timeout=10000).read()
                soup = BeautifulSoup(data, 'html.parser')
                finalData['drlouming'] = member['drlouming']
                finalData['drceng'] = member['drceng']
                finalData['drfangjian'] = member['drfangjian']
                QUERY_URL = QUERY_URL2

            finalData['__VIEWSTATE'] = soup.find(id='__VIEWSTATE')['value']
            finalData['__VIEWSTATEGENERATOR'] = 'CA0B0334'


            finalData['__EVENTTARGET'] = 'drlouming'
            request = urllib2.Request(QUERY_URL, urllib.urlencode(finalData).encode('utf-8'))
            data = opener.open(request, timeout=10000).read()
            soup = BeautifulSoup(data, 'html.parser')

            finalData['__EVENTTARGET'] = 'drceng'
            finalData['__VIEWSTATE'] = soup.find(id='__VIEWSTATE')['value']
            request = urllib2.Request(QUERY_URL, urllib.urlencode(finalData).encode('utf-8'))
            data = opener.open(request, timeout=10000).read()
            soup = BeautifulSoup(data, 'html.parser')
            if member['port'] =='2':
                fare = soup.find(attrs={'class':'number orange'}).text
                print member['name'] + ':' + fare
                if string.atof(fare) < 10.0:
                   sendEmail(member['email'], fare)
                continue
            else:
                finalData['__EVENTTARGET'] = 'drfangjian'
                finalData['__VIEWSTATE'] = soup.find(id='__VIEWSTATE')['value']
                request = urllib2.Request(QUERY_URL, urllib.urlencode(finalData).encode('utf-8'))
                data = opener.open(request, timeout=10000).read()
                soup = BeautifulSoup(data, 'html.parser')
                fare = soup.find(attrs={'class':'number orange'}).text
                print member['name'] + ':' + fare
                if string.atof(fare) < 10.0:
                    sendEmail(member['email'], fare)

    except:
        print time.strftime( '%Y-%m-%d %X', time.localtime())
        print 'error'
        # 发送邮件给管理员
        sendEmail('', '-1')

if __name__ == '__main__':
    while True:
        main()
        print time.strftime( '%Y-%m-%d %X', time.localtime())
        time.sleep(60 * 60 * 30)
