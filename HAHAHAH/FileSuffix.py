import os, re
from urllib import request

'''
path = 'D:\\img2'
url = 'http://10.1.24.133/EaaS/Message/'
files = os.listdir(path)
urls = []
for file in files:
    print('Start to upload ' + file)
    with open(os.path.join(path, file), 'rb') as f:
        req = request.Request(url + file, f.read())
        res = request.urlopen(req).read().decode('utf-8')
    urls.append(url + file)
print(urls)
'''


def search_all_files(path):
    folders = os.listdir(path)
    for folder in folders:
        if os.path.isdir(os.path.join(path, folder)):
            search_all_files(os.path.join(path, folder))
        else:
            with open(os.path.join(path, folder), 'rb') as f:
                result = compiledRe.search(str(f.read()))
                if (result is not None):
                    print('Finded in: ' + os.path.join(path, folder))
                    print(result.group())

path = input('Welcome, input the path you want to search:')
if(path == ''):
    path = r'D:\trgit2\3PL\Portal\src'
# r'D:\trgit2\3PL\Portal\src':''
compiledRe = re.compile(input('And then, input a regular expression:'))

folders = os.listdir(path)
search_all_files(path)
