
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("How much tip do you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person) #pq o round pode não funcionar em todos os casos
print(f"Each person should pay ${bill_per_person}")