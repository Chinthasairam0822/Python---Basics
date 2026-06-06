"""GCD stands for Greatest Common Divisor.
  It means:
    The largest number that divides both numbers exactly."""
number1 = int(input("Enter a number : "))
number2 = int(input("Enter a number : "))
 
number1 = abs(number1)
number2 = abs(number2)
print("Factors of number 1 : ")
for i in range(1,number1+1):
    if number1 % i == 0:
        print(i)
print("Factors of number 2 : ")
for j in range(1,number2+1):
    if number2 % j == 0:
        print(j)

print("GCD is : ")
gcd = 1
for i in range(1,min(number1,number2)+1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
print(gcd)

        # The GCD of two numbers can never be greater than the smaller of the two numbers. 


