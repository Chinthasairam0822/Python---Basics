N = int(input("Enter value of N : "))
sum=0
print("Even numbers:")
for i in range(0,N+1,+2):
    print(i)
# sum of even numbers : 
for i in range(0,N+1,+2):
    sum = sum+i
print("Sum of even numbers : ",sum)