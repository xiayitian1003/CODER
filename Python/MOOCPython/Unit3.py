# n = int(input())
# total = 0
# for i in range(n):
#     total += int(input())
# avr = total / n
# print("%d %.5f" % (total, avr))

# n = int(input())
# numbers = list(map(int, input().split()))
# minv = maxv = numbers[0]
# for i in numbers:
#     if i < minv:
#         minv = i
#     if i > maxv:
#         maxv = i
# print(maxv - minv)

# n = int(input())
# gold, silver, bronze = 0, 0, 0
# for i in range(n):
#     medal = list(map(int, input().split()))
#     gold += medal[0]
#     silver += medal[1]
#     bronze += medal[2]
# print(gold, silver, bronze, gold + silver + bronze)

# n = int(input())
# args = list(map(int, input().split()))
# cocktail = args[1] / args[0]
# for i in range(n - 1):
#     args = list(map(int, input().split()))
#     cur = args[1] / args[0]
#     gap = cur - cocktail
#     if gap > 0.05:
#         print("better")
#     elif -0.05 <= gap <= 0.05:
#         print("same")
#     elif gap < -0.05:
#         print("worse")

# n = int(input())
# # strs = n + "/" + str(2)
# # print(strs)
# # strs = n + "/" + str(2)
# # print(strs+"=%d" % (eval(strs)))
# while n != 1:
#     if n % 2 == 0:
#         strs = str(int(n)) + "/2"
#         print(strs + "=%d" % (eval(strs)))
#         n = eval(strs)
#     elif n % 2 == 1:
#         strs = str(int(n)) + "*3+1"
#         print(strs + "=%d" % (eval(strs)))
#         n = eval(strs)
# else:
#     print("End")

# n = int(input())
# maxl = cur = int(0)
# for i in range(n):
#     ps = list(map(int, input().split()))
#     if (90 <= ps[0] <= 140) and (60 <= ps[1] <= 90):
#         cur += 1
#         if cur > maxl:
#            maxl = cur
#     else:
#         cur = 0
# print(maxl)

# n = int(input())
# ans = int(0)
# if n == 0:
#     print(ans)
# else:
#     if n > 0:
#         sign = True
#     elif n < 0:
#         sign = False
#         n = -n
#     while (n % 10) == 0:
#         n = n // 10
#     while n != 0:
#         ans = ans * 10 + n % 10
#         n //= 10
#     if sign:
#         print(ans)
#     else:
#         print(-ans)

# n = int(input())
# for a in range(7):
#     for b in range(7):
#         for c in range(1, 7):
#             if (a + b * 7 + c * 49) == (c + b * 9 + a * 81):
#                 print(a + b * 7 + c * 49)
#                 print(a + b * 10 + c * 100)
#                 print(c + b * 10 + a * 100)

# def have2(n):
#     value = int(n)
#     cnt = num = int(0)
#     loop_cnt = int(0)
#     while n > 0:
#         bits = n % 10
#         if bits < 2:
#             bits = n % 10
#             cnt = (bits + 1) * cnt
#         elif bits == 2:
#             bits = n % 10
#             cnt = (bits + 1) * cnt + value % (10 ** loop_cnt) + 1
#         elif bits > 2:
#             bits = n % 10
#             cnt = (bits + 1) * cnt + 10 ** loop_cnt
#         n //= 10
#     return cnt

# def have2(n):
#     num = n
#
#     n = int(n)
#     cnt = int(0)
#     while n != 0:
#         # print("have2")
#         if n % 10 == 2:
#             cnt += 1
#         n = n // 10
#     # if cnt > 0:
#     #     print(n, end=" ")
#     return cnt
#
#
# scope = list(map(int, input().split()))
# l, r = scope[0], scope[1]
# cnt = int(0)
# for i in range(l, r + 1):
#     cnt += have2(i)
# print(cnt)
# print(have2(l), have2(r))

#
#
# for i in range():
#     total = int(0)
#     for j in range(10 ** i):
#         total += have2(j)
#     print(10 ** i, total)

