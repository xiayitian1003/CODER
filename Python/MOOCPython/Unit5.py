# x = 4
# def f0():
#     print("x in f0:", x)  # 这个x是全局的x
#
#
# def f1():
#     x = 8
#     # 这个x是局部的x，不会改变全局的x
#     print("x in f1:", x)
#
#
# def f2():
#     global x
#     # 说明本函数中的x都是全局的x
#     print("x in f2:", x)
#     x = 5
#     print("x in f2:", x)
#
#
# def f3():
#     x = 9
#     print("x in f3=", x)
#     # 会出错。因后面有赋值而被当作局部的x，此处没赋值就先使 用了，不行
#
# f0()
# f1()
# print(x)
# f2()
# print(x)
# f3()

# numbers = list(map(int, input().split()))
# a, b = numbers[0], numbers[1]
# weekdays = "Monday","Tuesday","Wednesday","Thursday" \
#     ,       "Friday","Saturday","Sunday"
# print(weekdays)

# def big(x, y):
#     if x == y:
#         return int(0)
#     else:
#         cmp = x, y
#         x_bigger_y = -1
#         win = ((0, 2), (2, 5), (5, 0))
#         for i in win:
#             if cmp == i:
#                 x_bigger_y = 1
#     return x_bigger_y


# def who_win(i):
#     cur_a = i % l_a
#     cur_b = i % l_b
#     return big(na[cur_a], nb[cur_b])
#
#
# numbers = list(map(int, input().split()))
# win_a = win_b = int(0)
# n, l_a, l_b = numbers[0], numbers[1], numbers[2]
# na = tuple(map(int, input().split()))
# nb = tuple(map(int, input().split()))
#
# for i in range(n):
#     if who_win(i) == 1:
#         win_a += 1
#     elif who_win(i) == -1:
#         win_b += 1
#
# if win_a > win_b:
#     print("A")
# elif win_b > win_a:
#     print("B")
# else:
#     print("draw")

# strs = input()
# cnt = int(0)
# for i in range(len(strs)):
#     if ord('0') <= ord(strs[i]) <= ord('9'):
#         cnt += 1
# print(cnt)

# def flipLetter(s):
#     if s.isupper():
#         s = s.lower()
#     elif s.islower():
#         s = s.upper()
#     return s
#
#
# strs = input()
# # strs[0] = 'c'
# ans = ""
# for i in range(len(strs)):
#     ans += flipLetter(strs[i])
# print(ans)

# s = input().split()
# ans = ""
# for i in s:
#     ans += i + " "
# print(ans.rstrip())

# strs = input()
# findit = False
# for i in range(len(strs)):
#     if strs.count(strs[i]) == 1:
#         print(strs[i])
#         findit = True
#         break
#
# if findit == False:
#     print("no")

# strs = input()
# if strs == strs[::-1]:
#     print("yes")
# else:
#     print("no")

# s_list = input().split(",")
# s, s1, s2 = s_list[0], s_list[1], s_list[2]
# x1, x2 = s.find(s1), s.rfind(s2)
# if x1 > -1 and (x2 - x1) >= len(s1):
#     print(x2 - x1 - len(s1))
# else:
#     print("-1")

# n = int(input())
# for i in range(n):
#     s_list = input().split()
#     s1, s2 = s_list[0], s_list[1]
#     times = s1.count(s2)
#     if times > 0:
#         last_position = int(0)
#         for j in range(times):
#             print(s1.find(s2, last_position), end=" ")
#             last_position = s1.find(s2, last_position) + len(s2)
#         print("")
#     else:
#         print("no")
#

#Calender
# def
#
#
# def countDay(a, b, c):
#
#
#
# n = int(input())
# for i in range(n):
#     date = list(map(int, input().split()))
#     y, m, d = date[0], date[1], date[2]
#     if -1000000 <= y <= 1000000 and 0 <= m <= 12 and 0 <= d <= 31:
#         print(countDay(y, m, d))
#     else:
#         print("Illegal")