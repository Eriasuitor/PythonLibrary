# def f1(a):
#     return a**2
#
#
# def f2(a):
#     return a+1
#
#
# a = [1, 2, 3]
# b = (1, 2)
#
# c = [f1(x) + f2(y) for x, y in zip(a, b)]
# d = (f1(x) + f2(y) for x, y in zip(a, b))       # Return a generator. way 1 of 2
#
# e, f = b
# # e, f, g = b     # Wrong here
#
# print('c:', c)
# print('d:', d)      # Return a generator
# print('e:', e)
# print('f:', f)
#
# print(next(d))      # equal to d.__next_() but not suggested to us it, in python 2 use d.next()

# iterable object.

# for i in d:     # Generator is an iterable objects;
#                 # There is a .__iter__() ( Not suggested, please use iter() ) function who is iterable object.
#                 # And who can be used in for? But not iterator definitely
#     print(i)


# Way 2 of 2:
def iterator():
    a, b = 1, 1
    while (True):
        c = yield a
        a, b = b, a + b
        print(c)


it = iterator()

# for i in range(100):
#     print(next(it))

it.send(None)  # Like next(it) but be the first one, inout argument only to be None
print(it.send('123'))  # Output is 123, 1

#  All generators is iterator, not all iterators are generator
#  Tow conditions: have iter(x) function and has next(x) function
print(next(iter([1, 2, 3])))  # Like this, [1, 2, 3] is not a iterator, return 1 here

for i in [1, 2, 3]:
    print(i)  # 3 thins that for did: call [1, 2, 3] 's iter() function
    # call next() and handle StopIteration exception


assert isinstance([1, 2], list)
assert not isinstance((1), tuple)
assert isinstance((1,), tuple)

max(len(x.strip()) for x in open('1.xtx', 'r'))     # Return the max length in all line of this file
