N = int(input())
dots = []

for n in range(N):
    dot = list(map(int, input().split()))
    dots.append(dot)

dots.sort()

for i in dots:
    print(str(i).replace("[", "").replace("]", "").replace(",", ""))