N = int(input())
nums = list(map(int, input().split()))
prime = ['True' for c in range(max(nums)+1)]    # 최대 길이만큼 숫자의 방? 을 만들어줌

for i in range(2, max(nums)+1):    # 1은 소수가 아니기 때문에 2부터 시작함
    if prime[i] == 'True':           # 만약 리스트의 i번째가 False, 즉 소수이면
        prime[i] = i                # False 대신 i로 바꿔줌
        for j in range(i+1, max(nums)+1):    # i를 i로 나누면 1이니까 i+1부터 나눔
            if j % i == 0:         # 둘을 나눴을 때 나머지가 0이면 배수
                prime[j] = 'False'    # 즉 소수가 아님

cnt = 0    # 카운트해주는 부분
for num in nums:
    if num in prime:
        cnt += 1

print(cnt)