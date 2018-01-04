assert not all(("", 1, 2))
assert all((' ', 1, 2))
assert not all((' ', 0, 2))
assert not 0


def func(a):
    print(a)
    return a + 1


ret = filter(func, (1, 2, 3))
print(ret)      # Return Filter, and it iterator

print(list(ret))        # [1, 2, 3] too, didn't add


def func(a):
    print(a)
    return a + 1


ret = map(func, (1, 2, 3))
print(ret)      # Return Map, and it iterator

print(list(ret))        # [2, 3, 4], added


from functools import reduce


def func(a, b):
    print(a)        # 1 3 6
    return a + b


ret = reduce(func, range(1, 5))
print(ret)      # Return 10 = 1 + 2 + 3 + 4


# lambda

f = lambda x, y: x + y
print(f(2, 3))      # Return 5

print(reduce(lambda x, y: x * y, range(1, 5)))      # Return 24 = 1 * 2 * 3 * 4
