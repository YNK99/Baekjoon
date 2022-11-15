from itertools import permutations

N, M = map(int, input().split())

nums = [c for c in permutations(range(1, N+1), M)]
nums.sort()

for i in nums:
    print(" ".join(map(str, i)))