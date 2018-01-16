import urllib2, re

headers = {"User-Agent" : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
req = urllib2.Request(r'https://www.qiushibaike.com/hot/page/1/', headers = headers)
proxyHandler = urllib2.ProxyHandler({'http':'http://194.126.37.93:8080'})

opener = urllib2.build_opener(proxyHandler)
resp = opener.open(req).read()
# print repr(resp)
divs = re.finditer(r'article\sblock.*?author\sclearfix.*?'
                 r'<a.*?'
                 r'<h2>\s?(?P<author>.*?)\s?</h2>.*?'
                 r'content".*?<span>\s*(?P<content>.*?)\s*</span>\s*</div>.*?</div>'
                 , resp, re.S|re.X)
count = 1
# for it in divs:
#     print (str(count) + it.group('author') + ':\n').decode('utf-8').encode('gbk')
#     count += 1
#     print it.group('content').replace('<br/>', '\n').decode('utf-8').encode('gbk')
#     print
#
for it in divs:
    if(it.group().find('class="thumb"') == -1):
        print (str(count) + it.group('author') + ':\n')
        count += 1
        print it.group('content').replace('<br/>', '\n')
        print
