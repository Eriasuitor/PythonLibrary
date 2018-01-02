from urllib import request
import re
req = request.urlopen(r"https://mm.taobao.com/self/aiShow.htm?spm=719.7763510.1998643336.100.ni80NG&userId=458607786")
res = req.read().decode("GBK")
urls = re.findall('src="//(.{10,300}?)jpg"', res, re.S)
i = 60
for url in urls:
    print(url + 'jpg')
    f = open(str(i) + '.jpg', 'wb')
    f.write(request.urlopen('http://' + url + 'jpg').read())
    i = i + 1
