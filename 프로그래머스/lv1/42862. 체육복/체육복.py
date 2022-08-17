def solution(n, lost, reserve):
    reserve = sorted(reserve)
    lost = sorted(lost)
    students = [1] * n
    for r in reserve:
        students[r - 1] = 2
    for l in lost:
        students[l - 1] -= 1
    answer = 0
    for i in range(len(students)):
        case1 = ([0] + students)[:-1]
        case2 = (students[1:] + [0])
        if students[i] > 0:
            continue
        elif students[i] < 1 and case1[i] == 2:
            students[i] += 1
            students[i - 1] -= 1
        elif students[i] < 1 and case2[i] == 2:
            students[i] += 1
            students[i + 1] -= 1
        else:
            continue
            
            
    answer = students.count(1) + students.count(2)
            
    return answer