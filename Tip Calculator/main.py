#Greeting
print("Welcome to the tip calculator.")
# Ask for the total bill.
bill = float(input("What was the total bill? $"))
# Ask for tip percentage. (10%, 12% or 15%)
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
#Ask how many people to split the bill with
count_people = float(input("How many people to split the bill? "))
#Calculation
tip_as_percent = tip/100
total_bill = bill + (bill*tip_as_percent)
#Print how much each person should pay by rounding off to 2 decimal places
bill_per_person = total_bill / count_people
split = round(bill_per_person, 2)
split = "{:.2f}".format(split)
#print(f"text.. {variable})
print(f"Each person should pay: ${split}")