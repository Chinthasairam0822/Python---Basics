"""An Armstrong Number is a number that is equal to the sum of 
   its digits raised to the power of the number of digits."""

number = int(input("Enter number:"))
Actual_number = abs(number)
Real_number = abs(number)
sign =1
if number<0:
    sign=-1
    number = abs(number)
count =0
while number>0:
    number =number//10
    count=count+1
print("No of digits in a number : ",count)
sum =0
while Actual_number>0:
  last_digit = Actual_number % 10
  sum = sum + (last_digit**count)
  Actual_number = Actual_number // 10
print(" sum of  digits raised to the power of the number of digits",sum)

if Real_number == sum:
   print("....Given number is AMstrong number....")
else:
   print("....Given number is not an Amstrong number....")