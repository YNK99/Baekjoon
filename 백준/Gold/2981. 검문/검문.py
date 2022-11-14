# a를 m으로 나눈 나머지와 b를 m으로 나눈 나머지가 같다면,
# (a-b)는 m의 배수가 된다
# n, m의 공약수이자 n, m의 모든 공약수의 배수인 양의 정수
# -> 유클리드 호제법: 두 수의 최대공약수를 구할 수 있음
N = int(input())

paper = sorted([int(input()) for _ in range(N)])
paper = [paper[c] - paper[c-1] for c in range(1, len(paper))]

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

GCD = paper[0]
for idx in range(1, len(paper)):
    GCD = gcd(GCD, paper[idx])

result = set()
for i in range(2, int(GCD ** 0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
result = sorted(list(result))

print(" ".join([str(c) for c in result]))