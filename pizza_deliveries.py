print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

size_price = 0
pepperoni_price = 0
cheese_price = 0



if size == 'S':
    size_price = 15
    if add_pepperoni == 'Y':
        pepperoni_price = 2
    if extra_cheese == 'Y':
        cheese_price = 1

elif size == 'M':
    size_price = 20
    if add_pepperoni == 'Y':
        pepperoni_price = 3
    if extra_cheese == 'Y':
        cheese_price = 1

elif size == 'L':
    size_price = 25
    if add_pepperoni == 'Y':
        pepperoni_price = 3
    if extra_cheese == 'Y':
        cheese_price = 1

total_bill = size_price + pepperoni_price + cheese_price

print(f"Your final bill is: ${total_bill}.")
