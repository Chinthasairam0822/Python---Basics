number = int(input("Enter Numbers : "))
count=0
if number==0:
   count =1
else:
    count=0

while number>0:
    number = number//10
    count = count + 1
print("No of digits in number = ",count)