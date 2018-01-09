# sys and os... http://www.cnblogs.com/alex3714/Articles/5161349.html
import hashlib      # To encryption

m = hashlib.md5('hello world'.encode('utf-8'))      # Like hashlib.sha512(), using different algorithm
print(m.hexdigest())
m.update('123'.encode('utf-8'))     # hello world123's hash
print(m.hexdigest())

# Logging... http://www.cnblogs.com/yuanchenqi/articles/5732581.html
# ConfigParser... http://www.cnblogs.com/alex3714/Articles/5161349.html

# import a module will execute all code of destination.
# import x  print(x.a)
# import data, sys

from time import * #  as x

print(time())       # Not time.time() anymore

# Repeat function will use nearby function, not this definitely

# import a.b.c  # Wrong, need to from a.b import c

# import a package will Execute __init__.py file, import a module will execute all file

