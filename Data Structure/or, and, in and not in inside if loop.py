zip_code = "902101"
if len(zip_code) == 6:
    print('Valid')
else:
    print('Invalid')

'''or'''

if 5 > 8 or 7 < 11:
    print("At least one of the conditions is True!")

if "cat" == "cat" or "dog" == "donkey":
    print("At least one of the conditions is True!")

if "cat" == "cat" or "dog" == "dog":
    print("At least one of the conditions is True!")

if "apple" == "banana" or "orange" == "pear":
    print("Will this print? Nope!")

'''and'''
if 5 < 7 and "rain" == "rain":
    print("Both of those conditions evaluate to True")

if 5 < 7 and "rain" == "fire":
    print("This will not print because at least one of the two conditions is false")

if type("rain") == type("fire") and 5 < 7:
    print("This will not print because at least one of the two conditions is false")

value = 95
if 90 < value < 100:
    print("This is a shortcut for the win!")
    
'''in and not in'''
if "H" in "Hello":
    print("That character exists in the string!")