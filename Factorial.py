num = int(input("Enter a number : "))
if num<0:
    print("Factorail of this number does not exist")
    exit()
    
fact = 1
for i in range(1,num+1,+1):
    fact = fact*i
print("Factorial of a number "+ str(num) +" :" ,fact)

