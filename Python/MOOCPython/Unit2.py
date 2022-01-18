# n = input()
# print(2 ** int(n))

# args = input().split()
# x, a, b, c, d = float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4])
# fx = a * x ** 3 + b * x ** 2 + c * x + d
# # print(fx)
# print("%.7f" % fx)

# a = int(input())
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# nums = input().split()
# x, y = int(nums[0]), int(nums[1])
# if (-1 <= x <= 1) and (-1 <= y <= 1):
#     print("yes")
# else:
#     print("no")

# nums = input().split()
# a, b, c = int(nums[0]), int(nums[1]), int(nums[2])
# if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
#     print("yes")
# else:
#     print("no")

# strs = input().split()
# weight = int(strs[0])
# cost = 0
# if 0 < weight :
#     cost += 8
# if weight > 1000:
#     cost += ((weight - 1000 + 499) // 500 ) * 4
# if strs[1] == "y":
#     cost += 5;
# print(cost)

# N = float(input())
# if 0 <= N < 5:
#     ans = -N + 2.5
# elif 5 <= N < 10:
#     ans = 2 - 1.5 * (N - 3) * (N - 3)
# elif 10 <= N < 20:
#     ans = N / 2 - 1.5
# print("%.3f" % ans)

# args = input().split()
# nums = [int(args[0]), int(args[1])]
# if args[2] == "+" :
#     ans = nums[0] + nums[1]
# elif args[2] == "-":
#     ans = nums[0] - nums[1]
# elif args[2] == "*":
#     ans = nums[0] * nums[1]
# elif args[2] == "/":
#     if nums[1] == 0:
#         ans = "Divided by zero!"
#     else:
#         ans = nums[0] // nums[1]
# else:
#     ans = "Invalid operator!"
# print(ans)
# import math

# nums = input().split()
# pi = float(3.14159)
# h, r = int(nums[0]), int(nums[1])
# v = pi * r ** 2 * h
# t = 20000 // v
# if (20000 % v) > 0:
#     t += 1
# print(int(t))

# numbers = list(map(int, input().split()))
# n, x, y = numbers[0], numbers[1], numbers[2]
# n -= y / x
# if n >= 0:
#     print(int(n))
# else:
#     print(0)

# numbers = list(map(float, input().split()))
# a, b, c = numbers[0], numbers[1], numbers[2]
# delta = b ** 2 - 4 * a * c
# # print(delta)
# if delta == 0:
#     print("x1=x2=%.5f" % (-b / (2 * a)))
# elif delta > 0:
#     print("x1=%.5f;x2=%.5f" % ((-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a)))
# elif delta < 0:
#     real = float(0)
#     if b != 0:
#         real = -b
#     real, imagine = real / (2 * a), (-delta)**0.5 / (2 * a)
#     print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (real, imagine, real, imagine))

# a1, a2 = 5, 6
# print(a1, a2)
# a1 = a2 = 1
# print(a1, a2)
