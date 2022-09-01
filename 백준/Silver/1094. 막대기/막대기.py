sticks = [64]

X = int(input())

while sum(sticks) > X:
    shortest = min(sticks)
    sticks.append(shortest / 2)
    sticks.append(shortest / 2)
    sticks.remove(shortest) 
    sticks.remove(shortest / 2)
    if sum(sticks) >= X:
        continue
    else:
        sticks.append(shortest / 2)

print(len(sticks))