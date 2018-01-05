# from keyword import kwlist
# for i in kwlist:
#     print(i)    # Watch all keep character
#
# dir(str)    # View the function and variable of a class or ?
# help(str)   # View the detail and description of a class or ?
#
# help(str.replace)
#
# s = [['a', 'b'], 1, 2, 3]
# s2 = s.copy()  # Shallow copy.Same as s3 = s[:]
# s3 = s  # This is not copy.
#
# s[1] = 4
# s2[2] = 4
# s3[3] = 4
# print(s)
# print(s2)
# print(s3)
#
# s2[0][1] = 'c'
# print(s)  # s2 is shallow copy so s'has changed there.
#
# s2[0] = "123"
# print(s2)
#
# import copy
#
# s4 = copy.copy(s)  # Shallow copy
# s5 = copy.deepcopy(s)  # Deep copy
#
# s4[0][0] = "555"
# s5[0][1] = "666"
# print(s, s5)
#
#
# # Set
#
# a = [[1, 2], "C"]
b = [1, 2, 3]
# # c = set(a)  # Will throw a exception here, [1, 2] is un hashable
d = set(b)
#
# # e = {d: "123"}  # Will throw a exception here, d is un hashable
# e = {"123": d}  # Right here
# # f = {"123", [1, 2, 3]}  # Will throw a exception here, [1, 2, 3] is un hashable
# print(e)
# # print(f)
#
# g = frozenset(b)
#
# e = {g: "123"}  # Right here
# e = {"123": e}  # Right here
# print(e)
#
# d.add("asd")    # asd will insert as a whole
# d.update("asd")  # a s d will insert respectively
d.update([1, 2, "123"])  # Same as above
# d.remove("asd")
# d.pop()  # Delete a value by fate
# d.clear()
print(d)

# del d

assert set("123") < set("1234")
assert set("123") == set("123123")
assert set("123") > set("12")

# assert (set("123") or set("34")) == set("3")  # Wrong
# assert (set("123") or set("34")) == set("1234")  # Wrong
# assert (set("123") and set("34")) == set("1234")  # Wrong

assert (set("123") | set("34")) == set("1234")  # Right
assert (set("123") & set("34")) == set("3")  # Right. plus sign + and ^ is as you wish

assert set("123").intersection(set("34")) == set("3")  # Like &
assert set("123").union(set("34")) == set("1234")  # Like |
assert set("123").difference(set("34")) == set("12")  # Like -
assert set("123").symmetric_difference(set("34")) == set("124")  # Like ^

assert set("123").issubset(set("1234"))
assert set("1234").issubset(set("1234"))
