from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    boat = deque([])
    cnt = 0

    while people != deque([]):
        boat.append(people.pop())
        
        if len(people) >= 1:
            boat.append(people.popleft())

            if sum(boat) > limit:
                people.appendleft(boat.pop())
                cnt += 1
                boat = deque([])

            else:
                cnt += 1
                boat = deque([])
        else:
            cnt += 1
                
    return cnt