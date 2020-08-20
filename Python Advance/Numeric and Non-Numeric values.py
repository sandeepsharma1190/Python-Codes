#########
user_input = int(input("Enter Number: "))
system_number = 10
if type(user_input) == int:
    print("Your number is ", user_input/system_number)
else:
    print("Not a number")
print('We will succeed one day')

####

user_input = input ('Enter your Number: ')
system_number = 10
try:
   val = int(user_input)
   print('Input is an integer number. Number = ', val/system_number)
   print('We will succeed one day')
except ValueError:
  try:
    val = float(user_input)
    print('Input is a float  number. Number = ', val/system_number)
    print('We will succeed one day')
  except ValueError:
      print('No.. input is not a number. It\'s a string')
      print('We will succeed one day')
finally:
    print('We will succeed one day')
    
