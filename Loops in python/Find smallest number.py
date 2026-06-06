n = int(input("How many numbers? "))
smallest = int(input("Enter 1st number : "))
for i in range(n-1):
     num = int(input("Enter number : "))
     if num<smallest:
          smallest =num
print("smallest number =", smallest)
      
     
