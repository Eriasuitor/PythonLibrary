# -*-coding:utf-8 -*-
# Code above to change default decode of this file ! default utf-8 in python 3, ASCII in python 2
import sys
print(sys.getdefaultencoding())     # Get default encoding of thi file.
# Not character's default encoding
# Python 3 use unicode decode default, Python 2 use ASCII decode default
s = "j见"
print("utf-8:", s)   # This type output code byte(maybe) in python 2, only.
# ss = s.decode("utf-8")
ss = s.encode("utf-8")
print(ss)    # decode() Default use ASCII decode and encode so is it.
# ss = s.decode("gbk")
# ss = s.encode("gbk")
print(ss.decode("utf-8"))
