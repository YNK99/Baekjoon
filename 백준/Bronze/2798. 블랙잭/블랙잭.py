N, M = map(int, input().split())
cards = list(map(int, input().split()))
card = cards
choose = []

for a in cards:
    for b in cards:
        for c in cards:
            if a + b + c <= M and len(set([a, b, c])) == 3:
                choose.append(a + b + c)

print(max(choose))