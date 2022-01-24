# T41-46



# n = int(input())
# lst = []
# for i in range(n):
#     score = tuple(input().split())
#     lst.append(score)
# lst.sort(key=lambda x: (-int(x[1]), x[0]))
# for i in range(len(lst)):
#     print(lst[i][0], lst[i][1])

# import copy
# args = list(map(int, input().split()))
# n, m = args[0], args[1]
# bitmap = []
# for i in range(n):
#     bitmap.append(list(map(int, input().split())))
# average = copy.deepcopy(bitmap)
# # print(average, bitmap)
# for i in range(1, n - 1):
#     for j in range(1, m - 1):
#         average[i][j] = round((bitmap[i][j] + bitmap[i - 1][j] + bitmap[i][j - 1] + bitmap[i][j + 1] + bitmap[i + 1][j]) / 5)
#
# for i in range(n):
#     for j in range(m):
#         print(average[i][j], end=" ")
#     print("")

# n = int(input())/>
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ans = int(0)
# for i in range(n):
#     ans += a[i] * b[i]
# print(ans)

# n = int(input())
# patient_old, patient_young = [], []
# for i in range(n):
#     patient = input().split()
#     patient[1] = int(patient[1])
#     if patient[1] >= 60:
#         patient_old.append(patient)
#     else:
#         patient_young.append(patient)
# patient_old.sort(key=lambda x: -x[1])
# patient_old.extend(patient_young)
# for i in patient_old:
#     print(i[0])


# def matrix_count(x, y):
#     cnt = int(0)
#     for i in range(m):
#         cnt += matrix_a[x][i] * matrix_b[i][y]
#     return cnt
#
#
# args = list(map(int, input().split()))
# n, m, k = args[0], args[1], args[2]
# # matrix_a = [[int(0) for i in range(m)] for j in range(n)]
# # matrix_b = [[int(0) for i in range(k)] for j in range(m)]
# matrix_a, matrix_b = [], []
# for i in range(n):
#     matrix_a.append(list(map(int, input().split())))
# for i in range(m):
#     matrix_b.append(list(map(int, input().split())))
# # print(matrix_a)
# # print(matrix_b)
# ans = [[0 for i in range(k)] for j in range(n)]
# # print(ans)
# for i in range(n):
#     for j in range(k):
#          print(matrix_count(i, j), end=" ")
#     print("")

# def isRecycled(s):
#     if reversed(s)


# strs = input()
# for i in range(2, len(strs) + 1):
#     start = int(0)
#     while start + i <= len(strs):
#         cur_str = strs[start: start + i]
#         if cur_str == cur_str[::-1]:
#             print(cur_str)
#         start += 1


