from urllib import request
req = request.urlopen("https://user.qzone.qq.com/2578507349?source=aiostar")
res = req.read().decode('utf-8')
print(res)
