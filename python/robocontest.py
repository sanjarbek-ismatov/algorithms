a = int(input())
c = 0
for i in range(1, a):
    x, y = map(int, input().split())
    c += x
d = int(input())
if (d - c >= 0):
    print(d - c)
else:
    print(0)
