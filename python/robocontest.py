# a = int(input())
# c = 0
# for i in range(1, a):
#     x, y = map(int, input().split())
#     c += x
# d = int(input())
# if (d - c >= 0):
#     print(d - c)
# else:
#     print(0)


# read input


# x1, y1, x2, y2 = map(int, input().split())
# xA, yA = map(int, input().split())
# # calculate slope and intercept of the line
# m = (y2 - y1) / (x2 - x1)
# b = y1 - m*x1

# # calculate coordinates of point B
# xB = (2*m*yA - 2*m*b + xA*(m**2 + 1) + 2*x1*m) / (m**2 + 1)
# yB = (m**2*yA + 2*b*m + y1*(m**2 + 1) - xA*m**2 - 2*x1*m) / (m**2 + 1)

# # write output

# print(str(int(xB)) + " " + str(int(yB)))


# Read input values from input.txt
# from math import ceil
from math import ceil
k, m, n = map(int, input().strip().split())
timePerCutlet = 2 * m
batches = ceil(n / k)
totalTime = batches * timePerCutlet
print(totalTime)


# t = int(input())

# for i in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     a.sort()
#     isAscending = all(a[j] - a[j-1] == 1 for j in range(1, n))

#     if isAscending:
#         print("YES")
#     else:
#         print("NO")

# n = int(input())

# sum_all = sum(range(1, n+1))  # sum of numbers from 1 to n
# sum_x_to_n = 0
# found_center = False

# for x in range(n, 0, -1):
#     sum_x_to_n += x
#     if sum_x_to_n == sum_all - sum_x_to_n + x:
#         print(x)
#         found_center = True
#         break

# if not found_center:
#     print(-1)

# Reading input from file

# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())

# # Checking if the move is possible for Horse
# diff_x = abs(x2-x1)
# diff_y = abs(y2-y1)
# if (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1):
#     print('YES')
# else:
#     print('NO')
