word = input("Enter a word: ")
count = 0
for ch in word:
   if ch.isalpha() and ch not in "aeiou":
      count = count+1
print("consonants in the word are:", count)