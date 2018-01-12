import urllib2, re

headers = {"User-Agent" : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
req = urllib2.Request(r'https://www.qiushibaike.com/hot/page/1/', headers = headers)
proxyHandler = urllib2.ProxyHandler({'http':'http://194.126.37.93:8080'})

opener = urllib2.build_opener(proxyHandler)
resp = opener.open(req).read()
# print repr(resp)
divs = re.findall(r'<div class="article block.*?>((.{0:5}<div>.*?</div>.{0:5})*)</div>', resp, re.S)
i = 0
print divs.__len__()
for div in divs:
    print div