"""A Spy Number is a number in which:
   Sum of digits = Product of digits"""

number = int(input("Enter number : "))
Actual_number = abs(number)
sign = 1
if number<0:
    sign = -1
    number = abs(number)

if number == 0:
    sum = 0
    product = 0
else:
    sum = 0
    product = 1

while number>0:
      last_digit = number % 10
      sum = sum + last_digit
      number = number // 10
print("Sum of digits = ",sum)

while Actual_number>0:
     last_digit = Actual_number % 10
     product = product * last_digit
     Actual_number = Actual_number // 10
print("Product of digits = ",product)

if sum == product:
     print("....It is spy number.....")
else:
     print("....It is not a spy number.....")