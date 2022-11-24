N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    age = int(age)    # int 형으로 꼭 바꿔야함ㅠㅠㅠ
    members.append([age, name])

members = sorted(members, key = lambda x:x[0])

for member in members:
    print(*member)