import urllib
import urllib2
import json

url_format = 'https://www.baidu.com/home/pcweb/data/mancardwater?id=2&offset=%d&sessionId=14832978921842&p_params=31415927&newsNum=3&indextype=manht&_req_seqid=0xf7e28ac600008a71&asyn=1&t=1483297904932&sid=1445_21093_20691_21554_21592'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
request_headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,en-US;q=0.8,en;q=0.6",
    'cookie': "BAIDUID=967E3B223D6EF159BEC8EDB441C8CA3E:FG=1; BIDUPSID=967E3B223D6EF159BEC8EDB441C8CA3E; PSTM=1484982290; BDUSS=nVvaXZmbFhTZlBNUDhPNXlYZlVYYU5OTm10N3UtMnk0bnJEV09yd2V3RVRKS3hZSVFBQUFBJCQAAAAAAAAAAAEAAAC4Qr0zzve5z7rNv9bB-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABOXhFgTl4RYR; pgv_pvi=6289754112; BD_HOME=1; H_PS_PSSID=1457_21098_20691_20719; BD_UPN=12314753",
    'cache-control': "no-cache",
    'postman-token': "ffd3e32c-3099-ffcb-576e-c77b9d9a83ab"
    }

data = urllib.urlencode(values)
html_doc = ''
for i in range(1,6):
	req = urllib2.Request(url_format % (i),headers=request_headers)
	response = urllib2.urlopen(req)
	page = response.read()
	page = page.replace('\\x22','Xx22').replace('\\', '').replace('Xx22', '\\"')
	response_obj = json.loads(page)
	html_doc += response_obj['html'].replace('\\"', '"').encode('utf-8')

fo = open('baidu.html', 'wb')
fo.write('<!DOCTYPE html><html><head><meta http-equiv=Content-Type content="text/html;charset=utf-8"><meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1"><meta content=always name=referrer><title></title></head><body>')
fo.write(html_doc);
fo.write('</body>')
fo.close()