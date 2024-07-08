# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.

# 🚨 Remember to remove the print statement above when you submit.
names_string = input('Digit the names with a "," after the name: ')

from random import randint

names = names_string.split(',') 
len_names = len(names)

names_choices = randint(0,len_names -1)
print(f"{names[names_choices].strip()} is going to buy the meal today!")