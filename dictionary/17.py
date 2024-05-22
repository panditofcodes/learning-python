vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}
word=input("Enter a word:")
for alpha in word:
    if alpha in vowels:
        vowels[alpha] += 1
print("In {}".format(word))
for v, ocr in vowels.items(): 
    print(f"vowel {v} comes {ocr} times in {word} ")