class Ancestors:
    def __init__(self):
        print('By Ancestors')
        print(self)
        self.name = 'Lory'

    def f1(self):
        print("Ancestors's f1:", self)
        self.sex = 'male'

    def f2(self):
        print("Ancestors's f2:", self)


class Father2(Ancestors):
    age = 23

    def __init__(self):
        print('By father2')
        print(self)
        self.name = 'Lory'

    def f1(self):
        print("father2's f1:", self)
        self.sex = 'male'
        super(Father2, self).f1()
        Ancestors.f1(self)
        print('Start to call f2 in Father2')
        self.f2()

    def f2(self):
        print("father2's f2:", self)


class Father(Ancestors):
    age = 23
    salary = 2700.00

    def __init__(self):
        print('By father')
        print(self)
        self.name = 'Lory'

    def f1(self):
        print("father's f1:", self)
        self.sex = 'male'

    def f2(self):
        print("father's f2:", self)

    def p1(self):
        print('p property method of Father')
        return 1

    def p2(self, value):
        print('p property_setter method of Father')

    def p3(self):
        print('p property_deleter method of Father')

    p = property(fget=p1, fset=p2, fdel=p3)


class Son(Father2, Father):
    bonus = 20000

    def __init__(self, *arg, **args):
        print('By song')
        print(self)
        print(arg)
        print(args)
        print(self.salary)
        self.salary = 7000.00

    @staticmethod       # Static method
    def static_method():
        print('Static method of Son')

    @classmethod
    def class_method(cls):
        print('class method of Son')
        print(cls)

    @property
    def property_method(self):
        print('property method of Son')
        return 1

    @property_method.setter
    def property_method(self, value):       # Have to add value
        print('property_setter method of Son')

    @property_method.deleter
    def property_method(self):
        print('property_deleter method of Son')

    def f2(self):
        print("son's f2:", self)
        super(Son, self).f2()   # 2 ways to call parents' function
        Father.f2(self)     # Above was effected by order. Son(Father2, Father).
        # print(self.name)    # Wrong here
        print(self.sex)
        print(self.age)
        print(self.salary)


# c1 = Son(1, 2, 'a', eria='Lory')
# c1.f1()
# c1.f2()
# print(Father.salary)        # Not changed, it's static argument
# print(c1.bonus)
# print(id(c1.bonus))
# c1.bonus = 12
# print(c1.bonus)
# print(id(c1.bonus))     # id changed
# print(Son.bonus)
# print(id(Son.bonus))
# Son.static_method()
# Son.class_method()      # <class '__main__.Son'>
# print(c1.property_method)       # Call like a parameter
# c1.property_method = 555
# del c1.property_method
# c1.p
# c1.p = 123
# del c1.p
'''
    By song
    <__main__.Son object at 0x0000027358432A58>
    (1, 2, 'a')
    {'eria': 'Lory'}
    father2's f1: <__main__.Son object at 0x0000027358432A58>
    Start to call f2 in Father2
    son's f2: <__main__.Son object at 0x0000027358432A58>
    father2's f2: <__main__.Son object at 0x0000027358432A58>
    father's f2: <__main__.Son object at 0x0000027358432A58>
    male
    23
    7000.0
    son's f2: <__main__.Son object at 0x0000027358432A58>
    father2's f2: <__main__.Son object at 0x0000027358432A58>
    father's f2: <__main__.Son object at 0x0000027358432A58>
    male
    23
    7000.0

'''


class Permissions:
    __i = 152       # Private

    def __f1(self):     # Private
        print("Yes")

    def __init__(self):
        self.name = 'Lory'
        print('init')

    def __call__(self, *args, **kwargs):
        print('call')

    def __int__(self):
        print('int')
        return 1

    def __str__(self):
        print('str')
        return 'i love you'

    # __add__(self, other)
    # __del__(self) Destruct method
    # __dict__()
    def __getitem__(self, item):    # p[item]: # Can return
        print(type(item))
        print(item)
        print(item.start)   # click slice to see more.
    # __setitem__(self, key, value) # Cannot    p[key] = value
    # __delitem__(self, key)    # Cannot, Del p[key]
    # __iter__(self)        # Iterate the result of this method, list, string is same as this. return a iterator
    # such as iter([1, 2, 3]) or yield. Own this method means iterable object.

    def __iter__(self):
        for i in range(10):
            print(i, end=' ')
            yield i


# p = Permissions()       # p is an object of Permissions, Permissions is an object of type
# # Every class inherit object class
# p()
# print(int(p))
# print(str(p))
# print(p.__dict__)
# print(Permissions.__dict__)     # <class 'slice'>
# p[1: 2: 3]         # slice(1, 2, 3)
# for i in p:
#     pass        #　0 1 2 3 4 5 6 7 8 9

# string = 'Lory is so handsome.'
# print(string[1: 20: 2])     # oyi ohnsm.

# meta class


# class Foo:
#
#     def f1(self):
#         print(1)

# -----Like----Below--------------


# def f2(self):
#     print('123Hello')
#
#
# Foo = type('Foo', (object,), {'f1': f2})    # Class name Foo, inherit object, f1 method.
#
# foo = Foo()
# foo.f1()        # 123Hello, all class is an object of type.


class MyType(type):

    def __init__(cls, *args, **kwargs):
        print("MyType's inited method")
        super(MyType, cls).__init__(cls)

    def __call__(cls, *args, **kwargs):
        print("MyType's call method")
        obj = cls.__new__(cls, *args, **kwargs)
        obj.__init__(cls, *args, **kwargs)
        return obj      # Currently i believe that this is most reasonable explain.


class Foo2(object, metaclass=MyType):       # Declare that generate an object using MyType, not type anymore.

    # __metaclass__ = MyType    # Python2 spelled this.

    def __new__(cls, *args, **kwargs):
        print("Foo2's new method")
        return object.__new__(cls, *args, **kwargs)       # This object is foo2!

    def __init__(self, *args, **kwargs):
        print("Foo2's init method")

    def f1(self):
        print("Foo2's f1 method")

# output MyType's inited method. because you invoke MyType('Foo2', (object,), ...)


foo2 = Foo2()       # MyType's inited method    MyType's call method    Foo2's new method   Foo2's init method
foo2.f1()
