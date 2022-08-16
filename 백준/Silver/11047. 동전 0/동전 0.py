N, K = map(int, input().split())
coin_kind = []

for n in range(N):
    C = int(input())
    coin_kind.append(C)

coin_kind = coin_kind[::-1]

cnt = 0

for c in coin_kind:
    if K // c == 0:
        continue
    else:
        cnt +=  K // c
        K = K - (K // c) * c

print(cnt)