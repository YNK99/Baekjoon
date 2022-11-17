# 최소 비용으로 주유하여 목적지까지 가는 문제
# 이게... 그리디 풀이법인가...?

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]   # 마지막 도시의 기름값은 필요 없음

cost = 0
last_price = price[0]   # 처음값은 첫번째 도시의 기름값

for i in range(N - 1):
    if price[i] > last_price:             # 현재 기름값이 저번 기름값보다 크다
        cost += road[i] * last_price    # 그럼 저번 기름값 * 갈 도로 길이
    else:                                 # 현재 기름값이 저번 기름값보다 작거나 같다
        cost += road[i] * price[i]      # 그럼 현재 기름값 * 갈 도로 길이
        last_price = price[i]             # 그리고 바로 저번 기름값을 업데이트

print(cost)
