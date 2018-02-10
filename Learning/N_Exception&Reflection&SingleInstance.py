
class MyException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    intList = [1, 2]
    # intList[2]
    # int('I')
    assert 1 == 3
    raise MyException('Throw a my exception here.')
    raise Exception('Throw a exception here.')
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("All Right")
finally:
    print("Try Ended")

b = 'message'
f = '__str__'
myException = MyException('Error message')

print(getattr(myException, b))

print(hasattr(myException, 'code'))

setattr(myException, 'code', '404')

print(myException.code)

delattr(myException, 'message')

try:
    print(myException.message)
except Exception as e:
    print(e)
setattr(myException, b, 'Hello')
print(getattr(myException, f)())


class SingleInstance:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = SingleInstance()
            return cls.__v


print(SingleInstance.get_instance())
print(SingleInstance.get_instance())


