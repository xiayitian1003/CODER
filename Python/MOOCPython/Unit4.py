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

def big(x, y):
    if x == y:
        return int(0)
    else:
        cmp = x, y
        x_bigger_y = -1
        win = ((0, 2), (2, 5), (5, 0))
        for i in win:
            if x == i:
                x_bigger_y = 1
    return x_bigger_y


def who_win(i):
    cur_a = i % l_a
    cur_b = i % l_b
    return big(na[cur_a], nb[cur_b])

numbers = list(map(int, input().split()))
win_a = win_b = int(0)
n, l_a, l_b = numbers[0], numbers[1], numbers[2]
na = tuple(map(int, input().split()))
nb = tuple(map(int, input().split()))

for i in range(n):
    if(who_win(i) == 1):
        win_a += 1
    elif(who_win(i) == -1):
        win_b += 1

if win_a > win_b:
    print("A")
elif win_b > win_a:
    print("B")
else:
    print("draw")

