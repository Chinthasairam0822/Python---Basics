"""A Neon Number is a number where:
   Sum of the digits of its square = The original number"""


number = int(input("Enter number : "))
Actual_number = abs(number)
sign = 1
if number<0:
    sign = -1
    number = abs(number)

square_of_a_number = number**2
squ_number = abs(square_of_a_number)

total =0

while square_of_a_number>0:
      last_digit = square_of_a_number % 10
      total = total + last_digit
      square_of_a_number = square_of_a_number // 10
print("Sum of the digits of its square = ",total)


if total == Actual_number:
     print("....It is Noen number.....")
else:
     print("....It is not a Neon number.....")