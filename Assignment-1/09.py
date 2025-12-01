text = input("Enter a paragraph: ")
text = text.title()
clean_text = " ".join(text.split())
vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
for ch in clean_text.upper(): 
    if ch in vowels:
        vowels[ch] += 1
print(clean_text)
print("Vowel Counts:")
for v, count in vowels.items():
    print(f"{v} ({ord(v)}): {count}")
