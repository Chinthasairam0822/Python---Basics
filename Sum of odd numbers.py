N = int(input("Enter value of N : "))
sum =0
for i in range(1,N+1,+2):
    print(i)
# sum of odd numbers : 
for i in range(1,N+1,+2):
    sum = sum+i
print("Sum of odd numbers : ",sum)