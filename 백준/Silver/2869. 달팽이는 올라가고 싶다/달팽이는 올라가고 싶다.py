import math

A, B, V = map(int, input().split())

oneday = A - B
top = V - B

print(math.ceil(top / oneday))