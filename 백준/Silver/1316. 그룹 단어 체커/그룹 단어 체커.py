N = int(input())

last = ""
cnt = 0

for n in range(0, N):
    word = input()
    word_alpha = set()
    word_alpha = set([c for c in word])
    last = ""
    for w in word:
        if last == "" or last == w:
            # cnt+=1
            last = w
        else:
            if w not in word_alpha:
                cnt += 1
                break
            else: 
                word_alpha.remove(last)
                last = w
        last = w
        
print(N - cnt)