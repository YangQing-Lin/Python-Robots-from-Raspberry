# 1
# i = 1
# while i<=100:
#     if(i % 2 == 1):
#         print(i)
#     i+=1

# answer
# for i in range(1, 101):
#     if i % 2 == 1:
#         print(i)
####################
# 2  wrong!!!
# string1 = "你好$$$我正在学 python@#@#现在需要&*&*&修改字符串"
# for each in string1:
#     if each=='$' || each=='@' || each=='#' || &

# answer 1
# string1 = "你好$$$我正在学 python@#@#现在需要&*&*&修改字符串"
# string2 = string1.replace('$$$', ' ').replace('@#@#', ' ').replace('&*&*&', ' ')
# print(string2)

# answer 2
# import re
# str1 = "你好$$$我正在学 python@#@#现在需要&*&*&修改字符串"
# str2 = re.sub('[$@#&*]', ' ', str1)
# print(str2)
####################
# 3
# i = 1
# j = 1
# while i <= 9:
#     j = i
#     while j <= 9:
#         print(i, '*', j, '=', i*j, ' ', end='', sep="")
#         j += 1
#     print()
#     i += 1

# answer
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%dx%d=%d\t" % (j, i, i*j), end="")
#     print("")
###################
# 4
# wrong!
# def money(i):
#     sum = 0
#     i = i / 10000
#     if i < 10:
#         sum += i * 0.1
#     elif i < 20:
#         sum = 1 + (i-10)*0.75
#     elif

# answer 1
# def calcute_profit(I):
#     I = I / 10000
#     if I <= 10:
#         a = I * 1.0
#         return a * 10000
#     elif I <= 20:
#         b = 0.25 + I * 0.075
#         return b * 10000
#     elif I <= 40:
#         c = 0.75 + I * 0.05
#         return c * 10000
#     elif I <= 60:
#         d = 1.55 + I * 0.03
#         return d * 10000
#     elif I <= 100:
#         e = 2.45 + I * 0.015
#         return e * 10000
#     else:
#         f = 2.95 + I * 0.01
#         return f * 10000
#
#
# I = int(input('净利润：'))
# profit = calcute_profit(I)
# print('利润为%d元是，应发奖金总数为%d元' % (I, profit))

# answer 2
# def calcute_profit(I):
#     arr = [1000000, 600000, 400000, 200000, 100000, 0]
#     # 这应该就是哥哥分界值，把它们放在列表里方便访问
#     rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
#     # 这是各个分界值所对应的奖金比例值
#     r = 0     # 这是总奖金的初始值
#     for idx in range(0, 6):
#         if I > arr[idx]:
#             r = r + (I - arr[idx]) * rat[idx]
#             I = arr[idx]
#     return r
#
#
# I = int(input('净利润：'))
# profit = calcute_profit(I)
# print('利润为%d元时，英法奖金总数为%d元' % (I, profit))
###################
# 5
# key - value : Page 21
# data = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# data1 = {}
# Max = 0
# temp = 0
# cnt = -1
# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[j] >= Max:
#             Max = data[j]
#             temp = j
#     data[temp] = cnt
#     data1[temp] = Max
#     Max = 0
# for value in data1.items():
#     print(value)

# answer
# I dont know
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
# awesome!
###################
# 6
# a = []
#
#
# def fun(a):
#     a.append(1)
#
#
# fun(a)
# print(a)


# 7
# 7.1
# class Person:
#     name = "aaa"
#
#
# p1 = Person()
# p2 = Person()
# p1.name = "bbb"
# print(p1.name)
# print(p2.name)
# print(Person.name)

# 7.2
# class Person:
#     name = []
#
#
# p1 = Person()
# p2 = Person()
# p1.name.append(1)
# print(p1.name)
# print(p2.name)
# print(Person.name)



