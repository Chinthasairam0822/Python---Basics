Principal_interest = int(input("Enter amount = "))
Rate_of_interest = int(input("Enter Interest in % = "))
Time_duration = int(input("Enter Time duration = ")) #measured in years // if you have to caluclate in months then TIme_duration/12
Simple_interest = (Principal_interest*Rate_of_interest*Time_duration)/100
print("Simple Interest = ", Simple_interest)