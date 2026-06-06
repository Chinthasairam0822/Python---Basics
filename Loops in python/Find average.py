n = int(input("How many numbers? "))
total = 0
for i in range(n):
    num = float(input("Enter number: "))
    total = total + num
average = total / n
print("Average =", average)