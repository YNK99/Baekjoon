N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append(word)

words = sorted(list(set(words)))
sorted_words = []

for _ in range(len(words)):
    sorted_words.append(min(words, key = len))
    words.remove(min(words, key = len))

for word in sorted_words:
    print(word)