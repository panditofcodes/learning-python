word = input("Enter a word or sentence:")
print(word)
alpha_set = {}

for a in word:
        if a in alpha_set:
            alpha_set[a] += 1
        else:
              alpha_set[a] =1
for value, occur in alpha_set.items():
      print(value," occurres ",occur)