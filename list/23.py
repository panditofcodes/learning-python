vowels = ['a','e','i','o','u']
words = input("Enter the words:")
found_vowels=[]
for letter in words:
    if letter in vowels:
        if letter not in found_vowels:
            found_vowels.append(letter)
print("The number of different vowel present ",words,"is",len(found_vowels), "and vowels are {}.".format(found_vowels))