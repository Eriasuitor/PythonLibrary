
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
