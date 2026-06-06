number1 = float(input("Enter a number 1 :"))
number2 = float(input("Enter a number 2 :"))
number3 = float(input("Enter a number 3 :"))

if number1 > number2:
      if number1 > number3:
             print(str(number1) + "is greater than " + str(number2) + "and" + str(number3))
elif number2 > number1 and number2 > number3:
      print(str(number2)  + "is greater than " + str(number1) + "and" + str(number3))
elif number3 > number1 and number3 > number2:
      print(str(number3)  + "is greater than " + str(number1) + "and" + str(number2))

else:
      print("Three numbers are equal")