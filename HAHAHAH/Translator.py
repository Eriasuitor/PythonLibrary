from urllib import request, parse
import gzip

values = {}
header = []
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
with open('YoudaoData', 'r', encoding='utf-8') as f:
    for i in f:
        ii = i.split(':', 1)
        values[ii[0]] = ii[1].replace("\n", "")
values['i'] = '存储库'
data = parse.urlencode(values).encode(encoding='UTF8')
req = request.Request(url, data)
print(data)
with open('YoudaoHeader', 'r') as f:
    for i in f:
        ii = i.split(':', 1)
        req.add_header(ii[0], ii[1].replace('\n', ''))
req.add_header('Content-Length', data.__len__())
print(req.headers)
res = request.urlopen(req).read().decode('utf-8')
res = eval(res)
print(res)
