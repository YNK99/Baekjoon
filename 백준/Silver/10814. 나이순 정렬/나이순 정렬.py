N = int(input())
members =[]

for _ in range(N):
    age, name = list(input().split())
    members.append([int(age), name])

sorted_members = sorted(members, key = lambda x:x[0], reverse = False)

for i in sorted_members:
    print(i[0], i[1])