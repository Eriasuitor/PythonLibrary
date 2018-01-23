try:
    intList = [1, 2]
    # intList[2]
    # int('I')
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
