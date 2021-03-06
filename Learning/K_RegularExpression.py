import re
# .
print(re.findall('Lory si so handsome', 'Lory si so handsome so'))
print(re.findall('L..y', 'Lory si so handsome so'))
print(re.findall('L(..)y', 'Lory si so handsome so'))
print(re.findall('me.so', 'Lory si so handsome\nso'))   # Only \n can't be matched
print(re.findall('me.so', 'Lory si so handsome\tso'))

# ^ Math the front
print(re.findall('L..y', 'Lory si so handsome\tso Lory'))
print(re.findall('^me.so', 'Lory si so handsome\tso'))
print(re.findall('^L..y', 'Lory si so handsome\tso Lory'))

# $ Match the end
print(re.findall('L..y$', 'Lory si so handsome\tso Lory'))

# * * can much 0 to +oo, pay attention to 0
print(re.findall('s*o', 'Lory si sssssso handsome\tso Lory'))       # There is o in answers
print(re.findall('L.*y', 'Lory si sssssso handsome\tso Lory'))      # ['Lory si sssssso handsome\tso Lory']
print(re.findall('.*', 'ILoveN'))       # Attention: answer is : ['ILoveN', '']

# + + can much 1 to +oo, pay attention to 1
print(re.findall('s+o', 'Lory si sssssso handsome\tso Lory'))       # There is not o in answers
print(re.findall('L.+y', 'Lory si sssssso handsome\tso Lory'))      #['Lory si sssssso handsome\tso Lory']
print(re.findall('.+', 'ILoveN'))       # Attention: answer is : ['ILoveN']

# ? ? can match 0 to 1
print(re.findall('s?o', 'Lory si sssssso handsome\tso Lory'))       # There is not o in answers
print(re.findall('L.?y', 'Lory si sssssso handsome\tso Lory'))      #['Lory si sssssso handsome\tso Lory']
print(re.findall('.?', 'ILoveN'))       # Attention: answer is : ['ILoveN']

# {} {x} repeat x times, {x, y} repeat x to y times         greed match!
print(re.findall('so{3}', 'sooo Lory is so hansome'))
print(re.findall('so{1,3}', 'sooo Lory is so hansomes'))        #print(re.findall('so{1, 3}', 'sooo Lory is so hansomes')) was wrong
# {1,} like +. {0, } like *.
print(re.findall('so{0,}', 'sooo Lory is so hansome'))
print(re.findall('so{,2}', 'sooo Lory is so hansome'))      # understand bu yourself

# []    # */+/? is not a special character in it
print(re.findall('L[o,l,s]ry', 'Lory isLory so handsome'))
# print(re.findall('L[o,l,s]{2}y', 'Lory isLory so handsome'))        # Why wrong?
print(re.findall('L[a-r, 1-9]{2}y', 'Lory isLo9y L,ryso handsome'))
print(re.findall('L[a-r1-9]{2}y', 'Lory isLo9y so hanLo,ydsome'))       # Same as above, No! above mean match a-r and , and 1-9
print(re.findall('L[*,o]ry', 'Lory isL*ry so handsome'))        # */+/? is not a special character in here, , is able to
print(re.findall('L[?,o]ry', 'Lory isL?ry so handsome'))
# */+/?... is not a special character in here, \ ^ - is not included.
print(re.findall('L[^?,o]ry', 'Lory isL?ry so handsome'))       # ^ is the not, means not ? and not o

# \ \d means number, \w means figure, \ can eliminate the special means of . / ^ /[ /] ...etc
'''
    \d [0-9]
    \D [^0-9]
    \s [\t\n\r\f\v]
    \S [^\t\n\r\f\v]
    \w [a-zA-Z0-9]
    \W [^a-zA-Z0-9]
    \b Special border of a word
'''
print(re.findall('\d{3}', '12345'))     # Answer is ['123'], not['123'] and ['234'] and ..
print(re.findall(r'I\b', 'youI Love N and LIST, I#/'))      # \b has special mean in python so we add r in front of it
print(re.findall(r'\bI', 'youI Love N and LIST, I#/'))

#######re.search() find the first onw who matched width and return a object

print(re.search('\.am', 'I.am so handsome'))
print(re.search('\.am', 'I.am so handsome').group())
print(re.search('\.an', 'I.am so handsome'))        # Return None when no matched string
print(re.findall(r'\\', '\you'))         # Difficult here
print(re.findall('\\\\', '\you'))

# ()
print(re.findall('as.*', 'asas'))
print(re.findall('(as)+', 'asas'))
print(re.findall('(as){2}', 'asas'))
print(re.search('(as)+', 'asas').group())       # Different in above and above

# |
print(re.findall('1|2', '14325541'))

# group(x)
ret = re.search('(?P<id>\w{3})\.(?P<name>\w*)\.', 'www.baidu.com')      # (?P<ID>  [RegularExpression] )
print(ret.group('id'))
print(ret.group('name'))

print(re.match('\w{3}I', '123I...132I').group())        # Match only the start

print(re.split('\d{3}', 'I154jfkhj451asjkfjklas123asd21wea'))
print(re.split('[,.]', 'I154jf,khj45.1asjk,.fjkl,as123,asd2,1w.ea'))

print(re.sub('a..b', '!..!','aloband soand a sb'))
print(re.sub('a\d*b', '!..!', 'a12345band soand a 123b'))

obj = re.compile('www.(\w*).com')
print(obj.findall('www.baidu.comwww.youku.com'))
print(obj.split('234234www.baidu.com123123www.youku.com'))      #['234234', 'baidu', '123123', 'youku', '']

# Add ? after "*","?","+","{m,n}" can make match ruler not greed.

print(re.search('a..b', 'asdasaxcbdasdbsd').span())


def func():
    i = 5
    print('Hello, ' + str(i))

# # .
# print(re.findall('Lory si so handsome', 'Lory si so handsome so'))
# print(re.findall('L..y', 'Lory si so handsome so'))
# print(re.findall('L(..)y', 'Lory si so handsome so'))
# print(re.findall('me.so', 'Lory si so handsome\nso'))   # Only \n can't be matched
# print(re.findall('me.so', 'Lory si so handsome\tso'))
#
# # ^ Math the front
# print(re.findall('L..y', 'Lory si so handsome\tso Lory'))
# print(re.findall('^me.so', 'Lory si so handsome\tso'))
# print(re.findall('^L..y', 'Lory si so handsome\tso Lory'))
#
# # $ Match the end
# print(re.findall('L..y$', 'Lory si so handsome\tso Lory'))
#
# # * * can much 0 to +oo, pay attention to 0
# print(re.findall('s*o', 'Lory si sssssso handsome\tso Lory'))       # There is o in answers
# print(re.findall('L.*y', 'Lory si sssssso handsome\tso Lory'))      # ['Lory si sssssso handsome\tso Lory']
# print(re.findall('.*', 'ILoveN'))       # Attention: answer is : ['ILoveN', '']
#
# # + + can much 1 to +oo, pay attention to 1
# print(re.findall('s+o', 'Lory si sssssso handsome\tso Lory'))       # There is not o in answers
# print(re.findall('L.+y', 'Lory si sssssso handsome\tso Lory'))      #['Lory si sssssso handsome\tso Lory']
# print(re.findall('.+', 'ILoveN'))       # Attention: answer is : ['ILoveN']
#
# # ? ? can match 0 to 1
# print(re.findall('s?o', 'Lory si sssssso handsome\tso Lory'))       # There is not o in answers
# print(re.findall('L.?y', 'Lory si sssssso handsome\tso Lory'))      #['Lory si sssssso handsome\tso Lory']
# print(re.findall('.?', 'ILoveN'))       # Attention: answer is : ['ILoveN']
#
# # {} {x} repeat x times, {x, y} repeat x to y times         greed match!
# print(re.findall('so{3}', 'sooo Lory is so hansome'))
# print(re.findall('so{1,3}', 'sooo Lory is so hansomes'))        #print(re.findall('so{1, 3}', 'sooo Lory is so hansomes')) was wrong
# # {1,} like +. {0, } like *.
# print(re.findall('so{0,}', 'sooo Lory is so hansome'))
# print(re.findall('so{,2}', 'sooo Lory is so hansome'))      # understand bu yourself
#
# # []    # */+/? is not a special character in it
# print(re.findall('L[o,l,s]ry', 'Lory isLory so handsome'))
# # print(re.findall('L[o,l,s]{2}y', 'Lory isLory so handsome'))        # Why wrong?
# print(re.findall('L[a-r, 1-9]{2}y', 'Lory isLo9y L,ryso handsome'))
# print(re.findall('L[a-r1-9]{2}y', 'Lory isLo9y so hanLo,ydsome'))       # Same as above, No! above mean match a-r and , and 1-9
# print(re.findall('L[*,o]ry', 'Lory isL*ry so handsome'))        # */+/? is not a special character in here, , is able to
# print(re.findall('L[?,o]ry', 'Lory isL?ry so handsome'))
# # */+/?... is not a special character in here, \ ^ - is not included.
# print(re.findall('L[^?,o]ry', 'Lory isL?ry so handsome'))       # ^ is the not, means not ? and not o and not ,
#
# # \ \d means number, \w means figure, \ can eliminate the special means of . / ^ /[ /] ...etc
# '''
#     \d [0-9]
#     \D [^0-9]
#     \s [\t\n\r\f\v]
#     \S [^\t\n\r\f\v]
#     \w [a-zA-Z0-9]
#     \W [^a-zA-Z0-9]
#     \b Special border of a word
# '''
# print(re.findall('\d{3}', '12345'))     # Answer is ['123'], not['123'] and ['234'] and ..
# print(re.findall(r'I\b', 'youI Love N and LIST, I#/'))      # \b has special mean in python so we add r in front of it
# print(re.findall(r'\bI', 'youI Love N and LIST, I#/'))
#
# #######re.search() find the first onw who matched width and return a object
#
# print(re.search('\.am', 'I.am so handsome'))
# print(re.search('\.am', 'I.am so handsome').group())
# print(re.search('\.an', 'I.am so handsome'))        # Return None when no matched string
# print(re.findall(r'\\', '\you'))         # Difficult here
# print(re.findall('\\\\', '\you'))
# print(re.findall('\\d', '5'))
# print(re.findall(r'\\d', '5'))
#
# # ()
# print(re.findall('as.*', 'asas'))
# print(re.findall('(as)+', 'asas'))
# print(re.findall('(as){2}', 'asas'))
# print(re.search('(as)+', 'asas').group())       # Different in above and above
#
# # |
# print(re.findall('1|2', '14325541'))
#
# # group(x)
# ret = re.search('(?P<id>\w{3})\.(?P<name>\w*)\.', 'www.baidu.com')      # (?P<ID>  [RegularExpression] )
# print(ret.group('id'))
# print(ret.group('name'))
#
# print(re.match('\w{3}I', '123I...132I').group())        # Match only the start
#
# print(re.split('\d{3}', 'I154jfkhj451asjkfjklas123asd21wea'))
# print(re.split('[,.]', 'I154jf,khj45.1asjk,.fjkl,as123,asd2,1w.ea'))
#
# print(re.sub('a..b', '!..!','aloband soand a sb'))
# print(re.sub('a\d*b', '!..!', 'a12345band soand a 123b'))
#
# obj = re.compile('www.(\w*).com')
# print(obj.findall('www.baidu.comwww.youku.com'))
# print(obj.split('234234www.baidu.com123123www.youku.com'))      #['234234', 'baidu', '123123', 'youku', '']
#
# # Add ? after "*","?","+","{m,n}" can make match ruler not greed.
#
# print(re.search('a..b', 'asdasaxcbdasdbsd').span())
#
# print(re.findall('a(.{1,100}?)b', 'accbfsdfsadfb')[0])      # Return cc not accb!
#
# print(re.findall('(\d)abc(?(1)\d|abc)', 'abcabcabc'))       # Something puzzled

# print(re.search('1(\s*?)2(\d)', '1\n\n\n\n\n\n\t\t\t\r\r23').group(2))
# print(re.match('1(\s*?)2(\d)', '21\n\n\n\n\n\n\t\t\t\r\r23').group(2))  # Wrong here, only match the front

# # m.pos, endpos, lastindex, lastgroup
# print(re.search('1(\s*?)2(\d)(\d)?', '1\n\n\n\n\n\n\t\t\t\r\r23').groups())
# print(re.search('1(\s*?)2(\d)(\d)?', '1\n\n\n\n\n\n\t\t\t\r\r23').groups('OOO'))
# print(re.search('1(?P<space>\s*?)2(?P<number>\d)', '1\n\t\t\t\r\r23').groupdict())     # Parameter like above
# print(re.search('1(?P<space>\s*?)2(?P<number>\d)', '1\n23').expand(r'\2--\1'))
#
# print(re.search('1(?P<space>\s*?)2(?P<number>\d)', '1\n\n\n\n\n\n\t\t\t\r\r23').span('space'))
# Retuen (.start('space'), .end('space'))

# re.finditer() use to match onr by one with iterator

'''
re 所定义的 flag 包括：

re.I 忽略大小写

re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境

re.M 多行模式

re.S 即为’ . ’并且包括换行符在内的任意字符（’ . ’不包括换行符）

re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库

re.X 为了增加可读性，忽略空格和’ # ’后面的注释
'''