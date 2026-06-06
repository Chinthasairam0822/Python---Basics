number1 = float(input("Enter a number 1 :"))
number2 = float(input("Enter a number 2 :"))

if number1 > number2:
      print( str(number1) + "is greater than " + str(number2))
elif number2 > number1:
      print(str(number2)  + "is greater than " + str(number1))
else:
      print("Both numbers are equal")