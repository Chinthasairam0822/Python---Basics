number = float(input("Enter a number : "))
if number%3==0 and number %7 == 0:
    print("Given number is divisible by both 5 and 11")
elif number%3==0 and number%7!=0:
    print("number is divisible by 5 but not with 11") 
elif number%3!=0 and number%7==0:
    print("number is not divisible by 5 but with 11")
else:
    print("number is not divisible by both 5 and 11") 
