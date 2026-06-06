"""What are Prime Factors?
    A prime factor is a factor (divisor) of a number that is also a prime number."""
number = int(input("Enter number: "))
number = abs(number)
print("Prime Factors are:")
for i in range(2, number + 1):
    if number % i == 0:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)