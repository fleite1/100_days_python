print('Welcome to the tip calculator')
bill = float(input("What was the total bill? "))
tip = int(input('How much tip would you like to give to the bartender? 10, 12 or 15 %? '))
people = int(input('How many people are with you? '))


tip_percent = tip / 100
total_tip = tip_percent * bill
total_bill = total_tip + bill

split_bill = total_bill / people

print(f'You need to pay {split_bill:.2f} tks')


