import urllib2
import json
from bs4 import BeautifulSoup

url_format = 'http://www.autohome.com.cn/grade/carhtml/%s.html';

request_headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'cookie': "ASP.NET_SessionId=x4skm3eeyrup1xhm4g3v3c5j; cookieCityId=110100; fvlid=1485090119298xz0qs5oQ; sessionip=124.205.188.242; sessionid=D0E06CDF-C45B-4B6A-A3B3-B0E70EE1C87D%7C%7C2017-01-22+21%3A02%3A01.307%7C%7C0; sessionuid=D0E06CDF-C45B-4B6A-A3B3-B0E70EE1C87D||2017-01-22+21%3A02%3A01.307||0; ahpvno=4; __utma=1.944097921.1485090121.1485090121.1485090121.1; __utmb=1.0.10.1485090121; __utmc=1; __utmz=1.1485090121.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ref=0%7C0%7C0%7C0%7C2017-01-22+21%3A15%3A16.728%7C2017-01-22+21%3A02%3A01.307; sessionvid=0686F4A6-50B3-4997-AFE0-2F5D28420D34; area=110199",
    'host': "www.autohome.com.cn",
    'if-modified-since': "Sun, 22 Jan 2017 13:00:08 GMT",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'postman-token': "8f6a0417-5aba-4b5b-cce3-f41eb134a5bd"
    }

try:
    fo = open('autohome1.html', 'r')
except IOError:
    html_doc = ''
    start_char = 'A'

    for i in range(ord('A'), ord('Z')):
        req = urllib2.Request(url_format % (chr(i)),headers=request_headers)
        response = urllib2.urlopen(req)
        page = response.read()
        html_doc += page;
    fo = open('autohome1.html', 'wb+')
    fo.write('<!DOCTYPE html>\
        <html>\
        <head>\
        <meta http-equiv=Content-Type content="text/html;charset=gb2312">\
        <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">\
        <meta content=always name=referrer>\
        <script type="text/javascript" src="jquery-3.1.1.min.js"></script>\
        <script type="text/javascript" src="autohome.js"></script>\
        <title>Autohome</title>\
        </head>\
        <body>\
        ')
    fo.write(html_doc);
    fo.write('</body>')

soup = BeautifulSoup(fo, "html.parser")

models_file = open("models.txt", "wb")

for model in soup.find_all("h4"):
    try:
        if model.string is not None:
            models_file.write("%s\r\n" % (model.string.encode('utf-8')))
    except ValueError:
        continue

fo.close()
models_file.close()