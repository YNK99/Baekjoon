from collections import deque

N = int(input())
cards = deque([c for c in range(1, N+1)])

cnt = 0

while len(cards) != 1:   # 카드의 개수가 1이 아닐 때까지
    cards.popleft()      # 가장 위 카드를 빼고
    P = cards.popleft()  # 가장 위 카드를 빼서
    cards.append(P)      # 맨 뒤에 추가

print(cards[0])