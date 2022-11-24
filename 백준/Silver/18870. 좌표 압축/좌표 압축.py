N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(set(nums))
r = list(range(N))
my_dict = dict(zip(sorted_nums, r))

for i, nums in enumerate(nums):
    print(my_dict[nums], end = ' ')