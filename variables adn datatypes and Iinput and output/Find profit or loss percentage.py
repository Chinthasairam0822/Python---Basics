Actual_price = int(input("Enter Actual price : "))
profit = float(input("Enter profit : "))
Loss = float(input("Enter Loss : "))

profit_percentage = (profit/Actual_price)*100
Loss_percentage = (Loss/Actual_price)*100

print("Profit precentage :",profit_percentage)
print("Loss precentage :",Loss_percentage)

overall_profit_percentage = profit_percentage - Loss_percentage 
print("Overall percentage = ",overall_profit_percentage)