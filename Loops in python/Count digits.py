number = int(input("Enter number : "))
sign = 1
if number<0:
    sign =-1
    number = abs(number)
count = 0
while number>0:
    number = number // 10
    count = count + 1
print("no of digits in a number : ",count)
