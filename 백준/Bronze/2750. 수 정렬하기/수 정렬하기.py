N = int(input())

nums = []

for _ in range(N):
    num = int(input())
    nums.append(num)

nums = sorted(nums)

for n in nums:
    print(n)