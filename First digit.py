number = int(input("Enter number : "))
sign = 1
if number<0:
    sign =-1
    number = abs(number)
while number>10:
    number = number//10

print("First digit = ",number)
