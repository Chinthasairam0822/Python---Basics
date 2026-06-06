number = int(input("How many terms: "))
n = int(input("Enter the nth term you have to know : "))
a= 0
b=1
print("Fibnocci series")
for i in range(number):
    print(a)
    next = a+b
    a= b
    b = next
for i in range(1,number):
    n = a
print(n)