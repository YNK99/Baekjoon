T = int(input())
N = [int(input()) for c in range(T)]
length = max(N)   # 했던 계산을 또 하지 않기 위해서 제일 큰 값으로 일단 다 계산
# 10번째까지는 규칙이 없으니까 리스트 만들어주고 거기에다 최대 길이만큼 되도록 0을 추가
memo = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * (length - 10)

idx = 10   # 10번째부터
for i in range(3, length - 10 + 3):    
    memo[idx] = memo[idx-1] + memo[idx-5]   # 점화식
    idx += 1

[print(memo[c-1]) for c in N]