#A Perfect Number is a number that is equal to the sum of its proper divisors.
"""What are proper divisors?  
      Proper divisors are all positive divisors of a number except the number itself."""

number = int(input("Enter number : "))
Real_number = abs(number)
sum =0
for i in range(1,number,+1):
    if  number % i == 0:
        sum = sum + i

if Real_number == sum:
    print("Perfect number")
else:
    print("Not a perfect number")