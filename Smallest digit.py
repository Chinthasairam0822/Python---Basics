number = int(input("Enter number : "))
sign = 1
if number<0:
    sign =-1
    number = abs(number)
smallest = 9
while number>0:
    last_digit = number % 10
    if last_digit < smallest:
        smallest = last_digit
    
    number = number//10
print("smallest digit in a number : ",smallest)