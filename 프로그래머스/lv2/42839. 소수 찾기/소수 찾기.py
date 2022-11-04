from itertools import permutations

def solution(numbers):
    a = 10 ** len(numbers)
    numbers = [c for c in numbers]
    possible_list = set()
    
    for i in range(1, len(numbers) + 1):
        possible_list.update(["".join(list(c)) for c in permutations(numbers, i)])
    
    prime_list = [False, False] + [True] * (a-1)
    prime_numbers = []

    for i in range(2, a + 1):
        if prime_list[i] == True:
            prime_numbers.append(i)
            for j in range(i*2, a+1, i):
                prime_list[j] = False
            
    return len({int(c) for c in possible_list if int(c) in prime_numbers})