def f1(a, b):
    print(a + b)


def f2(a, b, f):
    def f3(c, d):
        print(a ** b)

    f(a, b)
    return f3


f11 = f1
fx = f2(1, 2, f11)
fx(6, 2)        # Result is not 36, f3() is a closure, G will introduce it.
