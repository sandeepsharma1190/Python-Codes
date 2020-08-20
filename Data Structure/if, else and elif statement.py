if 5 > 3:
    print("Yup, that's true. This will be printed!")

if 6 > 10:
    print("Nope, that is FALSE. That will not be printed!")

if "Sandeep" == "Sandeep":
    print("Great name!")

if "sharma" == "Sharma":
    print("Awesome name")

if "sharma" == "Sharma":
    print("Haha, got you to print")
    print("Great success!")

'''Else statement'''
if 20 > 15:
    print("That is true!")
else:
    print("That is false!")

value = int(input("Enter a random number: "))

if value > 100000:
    print("I like that you're thinking big!")
else:
    print("That's an OK number, I guess")
        
'''Elif'''
def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither! It's zero"

print(positive_or_negative(5))
print(positive_or_negative(-3))
print(positive_or_negative(0))