#1st method 
"""character = input("Enter Character : ")
if (character>='A' and character<='Z') or (character>='a' and character<='z'):
    print("It is Alphabet")
else:
    print("It is not an ALphabet")"""


#2nd method -- python inbuilt function
ch = input("Enter character:")
if ch.isalpha():
    print("Alphabet")
else:
    print("Not Alphabet")