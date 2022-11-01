def solution(n, arr1, arr2):
    answer = 0
    map1 = ["0" * (n-len(format(c, 'b'))) + format(c, 'b') for c in arr1]
    map2 = ["0" * (n-len(format(c, 'b'))) + format(c, 'b') for c in arr2]
    final_map = []
    for i in range(n):
        row = ''
        for j, k in zip(map1[i], map2[i]):
            if int(j) == 0 and int(k) == 0:
                row += " "
            else:
                row += "#"
        final_map.append(row)
    return final_map