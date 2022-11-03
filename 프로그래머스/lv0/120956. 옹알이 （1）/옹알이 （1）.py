from itertools import permutations

def solution(babbling):
    can_say = []
    for i in range(1, 5):
        can_say += (["".join(c) for c in permutations(["aya", "ye", "woo", "ma"], i)])
    return len([c for c in babbling if c in can_say])