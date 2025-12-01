import string
sentence = input("Enter a sentence: ")

for p in string.punctuation:
    sentence = sentence.replace(p, "")

sentence = sentence.lower()
words = sentence.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

sorted_words = sorted(freq.items())
print("\nWord Frequencies:")
for word, count in sorted_words:
    print(f"{word}: {count}")
