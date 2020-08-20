# Tuple basic

foods = "Sushi", "Steak", "Guacamole"
foods = ("Sushi", "Steak", "Guacamole")

print(type(foods))

mystery = 1,
print(type(mystery))
empty = ()
print(type(empty))
print(tuple(["Sushi", "Steak", "Guacamole"]))
print(type(tuple(["Sushi", "Steak", "Guacamole"])))

birthday = (4, 12, 1991)
print(birthday[0])

employee = ("Bob", "Johnson", "Manager", 50)
first_name = employee[0]
last_name = employee[1]
position = employee[2]
age = employee[3]
first_name, last_name, position, age = employee
print(first_name, last_name, position, age)
'''or'''
first_name, last_name, *details = employee
print(details)
*names, position, age = employee
print(names)
first_name, *details, age = employee
print(details)
first_name, last_name, position, *details = employee
print(details)