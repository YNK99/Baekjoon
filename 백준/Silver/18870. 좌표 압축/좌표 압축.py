N = int(input())
X = list(map(int, input().split()))
sorted_X = {c[0]:c[1] for c in zip(sorted(set(X)), range(len(X)+1))}

for i in X:
    print(sorted_X[i], end = ' ')