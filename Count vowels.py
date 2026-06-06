word = input("Enter a word: ")
count = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1
print("Vowels in the word are:", count)