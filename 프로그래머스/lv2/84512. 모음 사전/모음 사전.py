from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(1, 6):
        words += [''.join(list(c)) for c in product(alpha, repeat = i)]
        
    words = sorted(words)
    
    return words.index(word) + 1