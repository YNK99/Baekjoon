N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k and j != k:
                nums = cards[i] + cards[j] + cards[k]
                if nums <= M and max_sum < nums:
                    max_sum = nums

print(max_sum)