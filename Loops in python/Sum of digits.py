number = int(input("Enter number : "))
sign = 1
if number<0:
    sign =-1
    number =abs(number)
sum =0
while number>0:
    last_digit = number % 10
    sum = sum + last_digit
    number = number//10
print("Sum of digits : ",sum)