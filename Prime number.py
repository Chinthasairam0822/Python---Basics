number = int(input("Enter number : "))

if number<1:
    print("it is not a prime number")
else:
    is_prime = True
for i in range(2,number):
    if number % i == 0:
        is_prime = False
        exit()
if is_prime:
        print("It is a prime number")
else:
        print("It is not a prime number")
 