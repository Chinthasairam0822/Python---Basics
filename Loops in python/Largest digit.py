number = int(input("Enter number : "))
sign = 1
if number<0:
    sign =-1
    number = abs(number)
largest = 0
while number>0:
    last_digit = number % 10
    if last_digit > largest:
        largest = last_digit
    
    number = number//10
print("Largest digit in a number : ",largest)