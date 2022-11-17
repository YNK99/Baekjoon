city = int(input())
length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
oil_price = oil_price[0:len(oil_price) - 1]
F = 0
last_price = 0

for c in range(0, city - 1, 1):    
    if c == 0:
        F = oil_price[0] * length[0]
        last_price = oil_price[0]

    else:
        if last_price >= oil_price[c]:
            F += oil_price[c] * length[c]
            last_price = oil_price[c]
        # 만약 저번 기름값이 지금 기름값보다 크거나 같으면:
        #     주유함
        #     요금 = 요금 + 지금 기름값 * 갈 거리
        else:
            F += last_price * length[c]
        # 만약 저번 기름값이 지금 기름값보다 작으면:
        #     요금 = 요금 + 저번 기름값 * 저번 갈 거리

print(F)