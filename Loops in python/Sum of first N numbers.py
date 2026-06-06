N = int(input("Enter value of N : "))
sum=0
print("Natural numbers:")
for i in range(1,N+1):
    print(i)
#sum of n natural numbers :
for i in range(1,N+1):
    sum = sum+i
print("Sum of" + str(N) +"natural numbers : ",sum)