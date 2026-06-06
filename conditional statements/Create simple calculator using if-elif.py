Number1 = float(input("Enter number : "))
Number2 = float(input("Enter number : "))
operator = input("Enter operator:")
if operator == '+':
    (print("Result : ",Number1 + Number2))
elif operator == '-':
    print("Result : ",Number1 - Number2)
elif operator == '*':
    print("Result : ",Number1 * Number2)
elif operator == '/':
    if Number2 != 0:
        print("Result =", Number1 / Number2)
    else:
        print("Division by zero is not possible")
elif operator == '%':
    if Number2 != 0:
        print("Result =", Number1 % Number2)
    else:
        print("modulus by zero is not possible")
elif operator == '//':
    if Number2 != 0:
        print("Result =", Number1 // Number2)
    else:
        print("Floor Division by zero is not possible")
elif operator == '**':
     print(Number1**Number2)
     
else:
    print("......Invalid operator.....")