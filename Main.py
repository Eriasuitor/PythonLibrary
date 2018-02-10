# print('-----------------What\'s man---------')
# temp = input('Guess a number:')
# guess = int(temp)
# if guess == 8:
#     print("What's the fuck, you are so diao")
#     print("But there is no bounes")
# else:
#     print("Wrong, the right number is 8")
# print('Game Over!')

# s = 'i=%E5%AD%98%E5%82%A8%E5%BA%93&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1514989455443&sign=4b926541b45fa94ffeb04acd2aa51a1c&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION&typoResult=false'
# print(s.__len__())

# a = 1
# print(type(a))
# a = '123'
# print(type(a))

# while True:
#     get = raw_input()
#     gets = [int(i) for i in get.split()]
#     envelopes = []
#     for i in range(gets[0]):
#         envelopeString = raw_input()
#         envelope = [int(j) for j in envelopeString.split()]
#         if(envelope[0] < gets[1] or envelope[1] < gets[2]):
#             continue
#         envelopes.append(envelope + [i])
#     envelopes = sorted(envelopes, key = lambda i: i[0])
#     envelopes.insert(0, [gets[1], gets[2], 0])
#     ans = [[0, []]]
#     for i in range(1, envelopes.__len__()):
#         ans.append([0, i])
#         for j in range(i):
#             if(envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1] and ans[j][0] >= ans[-1][0]):
#                 ans[-1][0] = ans[j][0] + 1
#                 ans[-1][1] = ans[j][1] + [envelopes[i][2]]
#     maxI = 0
#     for i in range(1, ans.__len__()):
#         if ans[i][0] > ans[maxI][0]:
#             maxI = i
#
#     print(ans[maxI][0])
#     print(' '.join(str(int(i) + 1) for i in ans[maxI][1]))

# get = raw_input()
# gets = [int(i) for i in get.split()]
# ans = []
# index = 1
# while True:
#     try:
#         patchString = raw_input()
#         patch = [int(i) for i in patchString.split()]
#         int(patch[0])
#         ans.append(patch + [index, 0, []])
#         index += 1
#     except:
#         break
# ans = sorted(ans, key = lambda k: k[1])
# ans.insert(0, [gets[0], gets[0], 0, 0, 0, []])
# for i in range(1, ans.__len__()):
#     for j in range(i):
#         if ans[i][0] <= ans[j][1] and (ans[i][4] > ans[j][4] + ans[i][2] or ans[i][4] == 0):
#             ans[i][4] = ans[j][4] + ans[i][2]
#             ans[i][5] = ans[j][5] + [i]
#
# minI = 0
#
# for i in range(1, ans.__len__()):
#     if(ans[i][1] >= gets[1] and (ans[i][4] < ans[minI][4] and ans[i][4] != 0 or ans[minI][4] == 0)):
#         minI = i
#
# tot = []
#
# tot.append(ans[ans[minI][5][0]][0])
# for i in ans[minI][5]:
#
#     tot.append(ans[i][1])
# print '->'.join(str(i) for i in tot) + '(' + str(ans[minI][4]) + ')'
#

countStr = '{44,954,123,54}'
valueStr = '{23,4,678,123}'
countStr = raw_input()
valueStr = raw_input()

count = [int(i) for i in countStr[1: -1].split(',')]
value = [int(i) for i in valueStr[1: -1].split(',')]

totPower = 0
dic = {}
for x, y in zip(count, value):
    totPower += x * y
    if y in dic:
        dic.update({y: x + dic[y]})
    else:
        dic.update({y: x})
print(dic)
if totPower % 2 == 1:
    print(0)
else:
    ans = [0] * (totPower / 2)
    ans.insert(0, 1)
    print(ans.__len__())

    for k, k2 in dic.items():
        i = ans.__len__() - 1
        while(i > 0):
            j = 1
            mi = min(k2, i / k) + 1
            while(j < mi):
                ans[i] += ans[i - k * j]
                j += 1
            i-=1

    print ans[-1]

#
# def isA(a):
#     i = 2
#     j = a / 2 + 1
#     while i <= j:
#         if a % i == 0:
#             return False
#         i += 1
#     else:
#         return True
#
# getString = raw_input()
# gets = [int(x) for x in getString.split()]
#
#
# ans = []
# while gets[0] <= gets[1]:
#     if isA(gets[0]):
#         if isA(gets[0] + 2 || gets):
#
#     gets[0] += 1
#
# print ans
# if ans.__len__() == 0:
#     print 'no'
# else:
#     ' '.join([str[i] for i in ans])
