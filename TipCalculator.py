total_bill = input("What's the total bill? $")
num_of_people = input("Between how many people should I split? ")
tip = input("What percentage of tip would you like to give? 10, 12 or 15: ")

bill_for_each = ( (float(total_bill) * ( int(tip) / 100 ) ) + float(total_bill)) / int(num_of_people)
bill_for_each = round(bill_for_each, 2)
print(f"Each person should pay ${bill_for_each}")
