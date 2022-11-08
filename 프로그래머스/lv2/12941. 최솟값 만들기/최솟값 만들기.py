def solution(A,B):
    list1, list2 = sorted(A), sorted(B, reverse = True)
    return sum([c[0] * c[1] for c in zip(list1, list2)])
    # 한 줄!
    # return sum([c[0] * c[1] for c in zip(sorted(A), sorted(B, reverse = True))])