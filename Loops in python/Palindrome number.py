# for numbers to check 
print("Original Number : ")
original_number = int(input("Enter number : "))
Actual_value = original_number
reverse_number = 0
sign = 1
if original_number < 0:
     sign = -1
     original_number =abs(original_number)
while original_number>0:
     last_digit = original_number % 10
     reverse_number = reverse_number*10 + last_digit
     original_number = original_number//10
print("Reverse Number : ",reverse_number)
if Actual_value == reverse_number:
     print(".....It is a palindrome....")
else:
     print(".....It is not a palindrome....")


# for words to check palindrome
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")