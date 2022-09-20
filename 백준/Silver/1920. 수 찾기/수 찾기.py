import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))

B = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

for m in M:
    start = 0
    end = len(A) - 1
    while True:
        if start <= end:
            mid = (start + end) // 2
            if A[mid] == m:
                print(1)
                break
            elif A[mid] > m:
                end = mid - 1
            else:
                start = mid + 1
        else:
            print(0)
            break