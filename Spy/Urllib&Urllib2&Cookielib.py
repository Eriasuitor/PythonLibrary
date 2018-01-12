import urllib2, cookielib, urllib

# data = urllib.urlencode(data)
# Wrong

# try:
#     headers = {"User-Agent" : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
#                "Referer": "http://www.zhihu.com/articles",
#                "Http":"http://194.126.37.93:8080",
#                "Proxy-Connection":"keep-alive"}
#     req = urllib2.Request(r'http://www.baidu.com',headers = headers)
#     req.get_method = lambda :'GET'
#     # req.headers = headers
#     resp = urllib2.urlopen(req)
#     print(resp.read())
# except urllib2.HTTPError, e:
#     print e.code
#     print e.reason      # reason is come from URLError, who is it's parents
# except urllib2.URLError, e:
#     print e.reason
# else:
#     print 'OK'

# urllib2.ProxyHandler({})

#ProxyHandler

# proxy_handler = urllib2.ProxyHandler({'http':'http://194.126.37.93:8080'})
#
# httpHandler  =urllib2.HTTPHandler(debuglevel=1)     # Will print log information in console
# httpsHandler  =urllib2.HTTPSHandler(debuglevel=1)
#
# opener = urllib2.build_opener(proxy_handler, httpHandler, httpsHandler)
#
# # urllib2.install_opener(opener)      # Install as default opener
# # print(urllib2.urlopen(r'http://www.baidu.com').read())
#
# print opener.open(r'http://www.baidu.com').read()

# cookielib

cookie = cookielib.CookieJar()
cookieFile = cookielib.MozillaCookieJar('cookieFromBaidu')
cookieHandler = urllib2.HTTPCookieProcessor(cookie)
cookirFileHandler = urllib2.HTTPCookieProcessor(cookieFile)
proxy_handler = urllib2.ProxyHandler({'http':'http://194.126.37.93:8080'})
openrCookieHandler = urllib2.build_opener(cookieHandler, cookirFileHandler, proxy_handler)
respCookieHandler = openrCookieHandler.open('http://www.baidu.com')     # Now cookie is assigned a value so can be
# used to post
print respCookieHandler.read()
# for item in cookie:
#     print type(cookie)      # Return <type 'instance'>
#     print item      # Return <Cookie BDSVRTM=0 for www.baidu.com/>
#     print item.name
#     print item.value

# for item in cookieFile:
#     print type(cookie)      # Return <type 'instance'>
#     print item      # Return <Cookie BDSVRTM=0 for www.baidu.com/>
#     print item.name
#     print item.value
# cookieFile.save(ignore_discard=True, ignore_expires=True)
#
# cookieFileFrom = cookielib.MozillaCookieJar()
# cookieFileFrom.load('cookieFromBaidu', ignore_discard=True, ignore_expires=True)
# for item in cookieFileFrom:
#     print type(cookie)      # Return <type 'instance'>
#     print item      # Return <Cookie BDSVRTM=0 for www.baidu.com/>
#     print item.name
#     print item.value
#
# req = urllib2.Request(r'http://www.baidu.com')
#
# response = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieFileFrom), proxy_handler).open(req).read()
# print response

# https://cuiqingcai.com/977.html
