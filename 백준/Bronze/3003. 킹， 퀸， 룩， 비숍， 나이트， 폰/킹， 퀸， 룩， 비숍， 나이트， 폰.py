white = list(map(int, input().split()))
black = [1, 1, 2, 2, 2, 8]

for i, j in zip(white, black):
    print(j - i)