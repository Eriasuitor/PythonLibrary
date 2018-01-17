# def pt(s, x, y='yes'):  # Default argument have to be after non-default argument
#     print(s, x, y)
#     return
#     print('%s %s' % (s, x))
#     return 1
#     return 1, '123', [1, 2]     # Return (1, '123', [1, 2])

# return None in default, return as so too

#
#


# print(pt("you are so", "handsome"))


# print(pt)
#
# pt(x="you are so", s="handsome")
#
#
# def pt():
#     print("Best")


# pt("you are so")  # Wrong here
# pt()
# print(pt)
#
# import time
#
# time_format = '%Y-%m-%d %X'
# timeCurrent = time.strftime(time_format)
# print(timeCurrent)
#
#
# def add(*args):
#     print(args)
#
#
# add(1)
# add(1, 2, 3)


def add(a='1', *args, **kkk):
    print(type(a))
    print(args)
    for i in kkk:       # No a
        print('%s : %s' % (i, kkk[i]))


add(1, [1, 2], number=[1, 2, 3], percentage=234)        # a is int
add(1, *[1, 2], number=[1, 2, 3], percentage=234)        # a is int, so you can use ** to post dic to **kkk
# add(number=[1, 2, 3], percentage=234)       # a is string
# add(number=123, percentage=234, 1, 2)       # Wrong here


# def add(**kkk, *args,):     # Wrong here. Default argument have to be after non-default argument anyway
#     print(args)
#     for i in kkk:
#         print('%s : %s' % (i, kkk[i]))

# def priority(name, age=22, *args, **kwargs):
#     pass


# Effect area

# if True:
#     a = 1
# print(a)
# In function there is wrong
"""
    built_in    int
    global      a = 1, a
    enclosing   Nested function
    local       in function
"""

b = 2


def f1():
    a = 1
    print("f1a:", a)
    print("f1b:", b)

    def f2():
        global b
        nonlocal a
        print("f21:", a)        # Wrong here if run with statements below. Right run it alone
        a = 2
        print("f2:", a)
        ''' 
        Like javascript, but a = 2 changed to var a = 2 in here. but why js say undefined but here 
        throw exception print("f22:", a)
        Maybe it's wrong the statement above...
        '''
        print(b)
        b = 4
        print(b)
    f2()
    print("f1a:", a)
    print("f1b:", b)

f1()
