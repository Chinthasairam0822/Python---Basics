number = int(input("Enter n8umber : "))
sign =1 
if number<0:
    sign = -1
    number = abs(number)
product = 1
while number>0:
    last_digit = number % 10
    product =product*last_digit
    number = number//10
print("Product of digits : ",product)