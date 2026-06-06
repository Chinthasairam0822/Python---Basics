number = int(input("Enter number : "))
sign = 1
if number<0:
    sign =-1
    number = abs(number)

last_digit = number % 10

print("last digit = ",last_digit)
