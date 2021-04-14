# List and Tuple 2
%%time      # will show taken time
l2 = [1,2,3,5]
l2.pop()
l2.pop(-2)

l2 = [1,2,3,5,5,5,5,5]
l2.remove(5)    # it will remove only one 5, we have to keep running syntax to remove 5
l2.reverse()

l = [[1,2],[3,4], [5,6], ['text', 'Data'],3,'4']
l.insert(1, 5+7j)
l.insert(3, [5,5])

# reverse
l[::-1]

# to reverse sublist
l[3][::-1]

#transferring string to list, it will seprate all the characters
a = 'test'
b = list(a)

# to print sublist values
l1 = ['lelel', 767858, 'ajkhfioj', [8789, 'fff']]
for i in l1:
    if type (i) == list:
        for j in i:
            print (j)
            print (type(j))

# to validate sublist values types
for i in l1:
    if type (i) == list:
        for j in i:
            print (type (j) == int)


# for addition of a list inside a list
l2 = ['lelel', 767858, 'ajkhfioj', [8789, 676, 'fff']]
for i in l2:
    if type(i) == list:
        n = 0
        for j in i:
            if type (j) == int:
                n = n+j
        print (n)
        
# To pull string from a list inside list
l2 = ['lelel', 767858, 'ajkhfioj', [8789, 676, 'fff', 'new']]
for i in l2:
    if type(i) == list:
        for j in i:
            if type (j) == str:
                print (j)

# To pull numbers from a list inside list
l2 = ['lelel', 767858, 'ajkhfioj', [8789, 676, 'fff', 'new']]
for i in l2:
    if type(i) == list:
        for j in i:
            if type (j) == int:
                print (j)


l2 = ['lelel', 767858, 'ajkhfioj', [8789, 676, 'fff', 'new']]
for i in l2:
    x = 0
    if type(i) == list:
        n = 0
        for j in i:
            if type (j) == int:
                n = n+j
        print (n)
    if type (l2) == int:
        x = x+n
    print (x)
    for x in l2:
        if type(l2) == int:
            x = x+n
    print (x)
            
for i in range (1,10):
    print (i)

# to print value in same line
str1 = 'Sandeep'
for i in str1:
    print (i, end = '')

list(range(1,7,-1))


a = ['a','4',['fg', 'ggfg']]
i = a.pop()
i.extend(a)


l1 = []
for i in a:
    if isinstance(i, list):
        l1.extend(i)
    else:
        l1.append(i)

# how to remove values from list and nested list
list1 = [4,5,6,5,3,[5,6,7,5,2, 5]]

# Below code will remove 5 from list, not from nested list
for i in list1:
    if i == 5:
        list1.remove(5)

# Below code will remove only one 5
for i in list1:
    if i == 5:
        list1.remove(5)
    if type(i) == list:
        i.remove(5)

# below code will remove 5 from list and nested list
for i in list1:
    if i == 5:
        list1.remove(5)
    if type(i) == list:
        for j in i:
            if j == 5:
                i.remove(j)     # we can use 5 here as well


# Taking input as a list, taking integers
# simple input always takes string as value
l = []
for i in range (5):     # it will take 5 inputs
    l.append(int(input('Enter any number: ')))
print (l)

# below code wont remove all characters
# b will take index of a, so "b" wont be removed, same with all characters
x = ['a','b','c','d','e']
for i in x:
    print (i)   # will show removed items
    x.remove(i)
print (x)

# list comprehension
l3 = [2,3,4,5,6]
[i**2 for i in l3]































