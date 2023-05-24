import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) >= 2:
            one = heapq.heappop(scoville)
            two = heapq.heappop(scoville)
            mixed = one + (two * 2)
            heapq.heappush(scoville, mixed)
            cnt += 1
        else:
            return -1
        
    return cnt