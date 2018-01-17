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


class Son(Father2, Father):
    def __init__(self, *arg, **args):
        print('By song')
        print(self)
        print(arg)
        print(args)
        self.salary = 7000.00

    def f2(self):
        print("son's f2:", self)
        super(Son, self).f2()   # 2 ways to call parents' function
        Father.f2(self)     # Above was effected by order. Son(Father2, Father).
        # print(self.name)    # Wrong here
        print(self.sex)
        print(self.age)
        print(self.salary)


c1 = Son(1, 2, 'a', eria='Lory')
c1.f1()
c1.f2()
'''
    By song
    <__main__.Son object at 0x000001C1D3A82668>
    (1, 2, 'a')
    {'eria': 'Lory'}
    father's f1: <__main__.Son object at 0x000001C1D3A82668>
    son's f2: <__main__.Son object at 0x000001C1D3A82668>
    father's f2: <__main__.Son object at 0x000001C1D3A82668>
    father's f2: <__main__.Son object at 0x000001C1D3A82668>
    male
    23
'''