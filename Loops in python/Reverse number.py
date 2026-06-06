number = int(input("Enter number : "))
# This part is for to handle negative numbers
sign = 1 
if number < 0:
    sign = -1
    number = abs(number)  # until here 

reverse = 0
while number>0:
    last_digit = number % 10
    reverse = reverse*10 + last_digit
    number = number//10
print("Reverse number : ",reverse)