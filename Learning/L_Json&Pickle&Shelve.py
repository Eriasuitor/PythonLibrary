import json
import pickle
from K_RegularExpression import func

dic = {"Lory": "Jiang", "Eria": "Li"}

with open('L_JsonByjson.txt', 'w') as f:
    f.write(json.dumps(dic))        # Like json.dump(dic, f)

with open('L_JsonByString.txt', 'w') as f:
    f.write(str(dic))

with open('L_FuncByPickle.txt', 'wb') as f:
    f.write(pickle.dumps(func))     # Like pickle.dump(func, f)

with open('L_JsonByjson.txt', 'r') as f:
    print(json.loads(f.read()))     # Like json.load(f)

# with open('L_JsonByString.txt', 'r') as f:
#     print(json.loads(f.read()))     # Wrong here

with open('L_FuncByPickle.txt', 'rb') as f:
    fun = pickle.loads(f.read())        # Like pickle.load(f)
    fun()

import shelve

f = shelve.open('L_Shelve')

f['name'] = 'Lory&Eria'
f.close()

f2 = shelve.open('L_Shelve')
print(f2['name'])
print(f2.get('name'))       # get will with None when not found, not throw a exception
print(f2)
