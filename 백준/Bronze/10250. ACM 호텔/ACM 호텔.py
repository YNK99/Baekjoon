T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    cnt = 0
    for w in range(1, W+1):
        for h in range(1, H+1):
            cnt += 1
            if cnt == N:
                if len(str(w)) == 1:
                    print(str(h)+str('0')+str(w))
                    break
                else:
                    print(str(h)+str(w))