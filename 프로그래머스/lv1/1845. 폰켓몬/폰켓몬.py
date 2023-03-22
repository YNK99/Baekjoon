def solution(nums):
    num = len(nums) // 2
    mons = {c:0 for c in nums}
    getcha = []
    
    for i in nums:
        mons[i] += 1
        
    for mon in mons.keys():
        if len(getcha) == num:
            break
        else:
            if mons[mon] == 0:
                del mons[mon]
            else:
                getcha.append(mon)
                mons[mon] -= 1
    return len(getcha)
