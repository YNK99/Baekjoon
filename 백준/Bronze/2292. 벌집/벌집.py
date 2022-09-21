N = int(input())

cnt = 0
rooms = 1

while rooms < N:
    if N == 1:
        break
    else:
        cnt += 1
        rooms += cnt * 6

print(cnt+1)