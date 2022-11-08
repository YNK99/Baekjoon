def solution(A,B):
    sorted_list = sorted([sorted(A), sorted(B, reverse = True)])
    list1, list2 = sorted_list[0], sorted_list[1]
    return sum([c[0] * c[1] for c in zip(list1, list2)])