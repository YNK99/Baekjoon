T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    c = 1
    for j in range(b):
        c = (c * a) % 10
    if c == 0:
        print(c + 10)
    else:
        print(c)