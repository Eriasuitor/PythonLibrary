import os, re
from urllib import request

path = 'D:\\img2 - Copy'
url = 'http://10.1.24.133/EaaS/Message/'
files = os.listdir(path)
urls = []
for file in files:
    # print('Start to upload ' + file)
    # with open(os.path.join(path, file), 'rb') as f:
    #     req = request.Request(url + file, f.read())
    #     res = request.urlopen(req).read().decode('utf-8')
    urls.append(url + file)
print(urls)