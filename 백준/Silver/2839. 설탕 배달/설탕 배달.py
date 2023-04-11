sugar = int(input())
dp = [5 for c in range(sugar // 5)] 

for i in range(20):
    if sugar == sum(dp):
        print(len(dp))
        break

    elif sugar - sum(dp) < 3 and 5 not in dp:
        print(-1)
        break
    
    elif (sugar - sum(dp)) % 3 != 0 and sugar - sum(dp) < 3:
        dp.pop(0)
        dp.append(3)
    else:
        dp.append(3)