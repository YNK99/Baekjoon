N = int(input())

schedule = []
schedule += ([list(map(int, input().split())) for _ in range(N)])
schedule = sorted(schedule, key = lambda x:(x[1], x[0]))

cnt = 0
last_end = 0
for i, j in schedule:
    if i >= last_end:
        cnt += 1
        last_end = j

print(cnt)