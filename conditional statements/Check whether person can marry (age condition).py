Age = int(input("Enter Age of a person :"))
Gender =input("Enter Gender of a person(M/F) : ")
if (Gender=='M' and Age>=21) or (Gender=='F' and Age>=18):
    print("Person is eligible to Marry")
else:
    print("Person is not eligible to Marry")