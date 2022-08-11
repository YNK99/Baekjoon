N, M = map(int, input().split())
total_bord = []
white_bord = []
black_bord = []
color = []

for i in range(8):
    if i % 2 == 0:
        white_bord.append("WBWBWBWB")
        black_bord.append("BWBWBWBW")
    else:
        white_bord.append("BWBWBWBW")
        black_bord.append("WBWBWBWB")

for n in range(N):
    chess = input()
    total_bord.append(chess)

for n in range(0, N + 1 - 8):
    for m in range(0, M + 1 - 8):
        cutting = [c[m:m+8] for c in total_bord[n:n+8]]
        C1 = 0
        C2 = 0
        for c1, w1, b1 in zip(cutting, white_bord, black_bord):
            for c2, w2, b2 in zip(c1, w1, b1):
                # print(c2, w2, b2)
                if c2 == w2:
                    C1 += 1
                else:
                    C2 += 1
        if C1 > C2:
            color.append(C2)
        elif C1 < C2:
            color.append(C1)
        else:
            color.append(C1)

print(min(color))