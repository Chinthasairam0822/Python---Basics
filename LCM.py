number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

number1 = abs(number1)
number2 = abs(number2)

lcm = max(number1, number2)

while True:
    if lcm % number1 == 0 and lcm % number2 == 0:
        break
    lcm = lcm + 1

print("LCM =", lcm)