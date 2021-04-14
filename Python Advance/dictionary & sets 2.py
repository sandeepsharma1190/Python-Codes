# dictionary & sets 2

dict1 = {1:2, 4:3, 'val':'val2'}

# to get all the keys
for i in dict1:
    print (i)
    
# to get all the values
for i in dict1:
    print (dict1[i])

for i in dict1:
    print (dict1)


dict2 = {1:2, 4:3, 'val':'val2', 'tup': (3,5,2,4)}
dict2.keys()

# to pull tuple values from a dictionary
for i in dict2.values():
    if type (i) == tuple:
        print (i)

# to append tuple values in a variable
m = []

for i in dict2.values():
    if type(i) == tuple:
        for j in i:
            m.append(j)


# to convert letters to upper case
list2 = ['python', 'love']
d = {}
for i in list2:
    d[i] = i.upper()

for i in list2:
    d[i] = i.isupper()



n = {}
for i in range(10):
    n[i] = i**2
# Comprehension operation
{i:i**2 for i in range(10)}
[i:i**3 for i in range(5)]  # invalid syntax, as it contains keys, list and tuples dont have keys










































