# Day 002: Tip Calculator

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percent / 100)
per_person_amount = round((total_bill + tip_amount) / people, 2)

print(f"Each person should pay: ${per_person_amount}")
