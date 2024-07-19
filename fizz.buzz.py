number =  100

for div in range (1,number +1):
    if div % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif div % 3 == 0:
        print("Fizz")
    elif div % 5 == 0:
        print("Buzz")
 
    else:
        print(div)
        
