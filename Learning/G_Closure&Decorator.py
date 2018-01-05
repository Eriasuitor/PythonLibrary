# def f2(a, b, f):
#     def f3(c, d):
#         print(a ** b)
#
#     f(a, b)
#     return f3
#
#
# f11 = f1
# fx = f2(1, 2, f11)
# fx(6, 2)        # Result is not 36, f3() is a closure, because it use a and b who are his enclose arguments.


# a = 3

#
# def f2():
#     def f3():
#         print(a)
#     print(a)
#     return f3
#
#
# f5 = f2()       # Return 3, not closure
# f5()        # Return 3, not closure



# import time
#
#
# def decorator(f):
#     def closure(*args):
#         start = time.time()
#         ret = f(*args)
#         print('%.20f' % (time.time() - start))
#         return ret
#     return closure
#
#
# @decorator('123')
# def add(*args):
#     tot = 0
#     for i in args:
#         tot += i
#     return tot
#
#
# print(add(*range(1, 101)))      # Return 5050, out 0.00000000000000 and 5050



import time


def logger(flag=False):
    def decorator2(f):
        def closure2(*args):
            start = time.time()
            ret = f(*args)
            print('%.20f' % (time.time() - start))
            if flag:
                print(ret)
            return ret
        return closure2
    return decorator2


@logger(True)       # = @decorator2
def add(*args):
    tot = 0
    for i in args:
        tot += i
    return tot


print(add(*range(1, 101)))      # Return 5050, out 0.00000000000000 and 5050
print(type('true'))     # Return str
