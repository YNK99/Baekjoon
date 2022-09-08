N = int(input())
nums = []

for n in range(N):
    num = int(input())
    nums.append(num)

sorted_nums = sorted(nums)

for i in sorted_nums:
    print(i)