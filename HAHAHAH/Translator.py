from urllib import request,parse

values = {}
header = []
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
with open('YoudaoData', 'r', encoding='utf-8') as f:
    for i in f:
        ii = i.split(':', 1)
        values[ii[0]] = ii[1].replace("\n","")
data = parse.urlencode(values).encode(encoding='UTF8')
req = request.Request(url, data)
with open('YoudaoHeader', 'r') as f:
    for i in f:
        ii = i.split(':', 1)
        header.append((ii[0], ii[1].replace('\n', '')))
        req.add_header(ii[0], ii[1].replace('\n', ''))
# openner = request.build_opener()
# openner.addheaders = header
# request.install_opener(openner)
# response = request.urlopen(url, parse.urlencode(data))

# req = request.Request(url, parse.ur(data))
# response = request.urlopen(req)
print(header)
req.add_header('Content-Length', data.__len__())
response = request.urlopen(req)
res = response.read()
# print(res.decode('utf-8', 'ignore'))
print(res.decode('url'))
# print(res)

