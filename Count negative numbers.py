n = int(input("How many numbers? "))
count = 0
for i in range(n):
    num = float(input("Enter number : "))
    if num < 0:
       count = count + 1
print("Negative numbers in a number are : ",count)