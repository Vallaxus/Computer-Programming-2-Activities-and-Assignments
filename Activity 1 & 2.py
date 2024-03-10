# Activity 1

vowel_pool = {'A', 'E', 'I', 'O', 'U'}
word = input("Enter a word: ").upper()
vowels = list()
nVowels = list()

for c in word:
    if c in vowel_pool:
        vowels.append(c)
    else:
        nVowels.append(c)

print("\nVowels: ", *vowels)
print("Non-vowels: ", *nVowels)

# Activity 2
