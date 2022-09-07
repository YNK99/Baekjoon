T = int(input())

floors = []
floors.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for i in range(14):
    floor = []
    for j in range(1, 15):
        floor.append(sum(floors[i][:j]))                  
    floors.append(floor) 

for t in range(1, T + 1):
    a = int(input())
    b = int(input()) - 1
    print(floors[a][b])