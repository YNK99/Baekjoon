N = int(input())

r = list(map(int, input().split()))
first = r[0]
rest = r[1:]

for i in rest:
    for j in range(i, 0 ,-1):
        if first % j == 0 and i % j == 0:
            print(str(first // j) + str("/") + str(i // j))
            break