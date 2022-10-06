def solution(array):
    my_dict = {c:0 for c in array}
    for i in array:
        my_dict[i] += 1
    c = sorted(my_dict.items(), key = lambda x:x[1], reverse = True)[:2]
    if len(c) == 1:
        print(1, c)
        return c[0][1]
    else:
        if c[0][1] == c[1][1]:
            print(2, c)
            return -1
        else:
            print(3, c)
            return c[0][0]