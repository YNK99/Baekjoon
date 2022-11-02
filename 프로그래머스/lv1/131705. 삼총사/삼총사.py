from itertools import combinations

def solution(number):
    cases = len([c for c in combinations(number, 3) if sum(c) == 0])
    return cases