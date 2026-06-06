# A Strong Number is a number whose value is equal to the sum of the factorials of its digits.
"""Armstrong → Digits raised to a power.
      Strong → Digits converted to factorials."""
number = int(input("Enter number : "))
Actual_number = abs(number)
sign =1
if number<0:
    sign=-1
    number = abs(number)

sum = 0
while number>0:
    last_digit = number % 10
    fact = 1
    for i in range(1,last_digit+1,+1):
        fact = fact * i
    sum = sum + fact
    number = number//10
print("sum of a factorials of a number : ",sum)

if Actual_number == sum:
    print("....Number is a strong number....")
else:
    print("....Number is not a strong number....")
