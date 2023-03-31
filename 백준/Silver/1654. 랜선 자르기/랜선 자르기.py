K, N = map(int, input().split())
lens = [int(input()) for c in range(K)]

start, end = 1, max(lens)
cnt = 0

while start <= end:

    mid = (start + end) // 2
    count = sum([c // mid for c in lens])

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)