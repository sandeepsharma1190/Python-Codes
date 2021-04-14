# More on While and For Loop

a = 10
b = 20

if a == 10 and b == 10:
    print ('True')
else:
    print ('Condition dint meet')


if a == 20 or b != 20:
    print ('True')
elif a == 10 or b == 20:
    print ('Cracked')
else:
    print ('Code dint work')


a1 = input ('Enter your first name: ')
b1 = input ('Enter your last name: ')

if a1 == 'Sandeep' or b1 == 'Sharma':
    print (a1, b1)
elif a1 == 'Rashmi' or b1 == 'Narula':
    print (b1, a1)
else:
    print ('Other name: ', a1, b1)


initial_speed = 0
final_speed = 100
count = 1
while initial_speed <= final_speed:
    print (initial_speed, final_speed)
    if initial_speed <= 40:
        print ('Slow Speed')
    elif initial_speed <= 60:
        print ('Speed is fine')
    elif initial_speed <= 80:
        print ('You are on high speed')
    else:
        print ('slow down')
    initial_speed+=10    
    count += 1
    if count == 9:
        break


bacon = 22
bacon + 1



(5 > 4) and (3 == 5)


n = 5
i = 1
j = 1
while i <= n:
    print (i)
    i+=1
else:
#    i = 1
    while j <= 2:
        print (j)
        j+=1
    print ('N/A')


s = 'Sandeep'
for i in s:
    if i == 'e':
        print ('we are in mid')
    print (i)


s = 'Sandeep'
for i in s:
    if i == 'e':
        print ('we are in mid')
    print (i)
else:
    print ('ending')


s = 'Sandeep'
for i in s:
    if i == 'e':
        print ('we are in mid')
    print (i)
else:
    if i == 'd':
        print ('d is in the exact mid of the name')
    print ('ending')


s = 'Sandeep'
for i in s:
    if i == 'e':
        break
    print (i)
else:
    if i == 'd':
        print ('d is in the exact mid of the name')
    print ('ending')


s = 'Sandeep'
for i in s:
    if i == 'e':
        continue
    print (i)
else:
    if i == 'd':
        print ('d is in the exact mid of the name')
    print ('ending')


s = 'Hello world'
ss = ''

for i in range(len(s)):
    if s[i] == 'o':
        continue
    else:
        ss+=s[i]

#################################################################################
s = 'Sandeep'
for i in s:
    if s[i] == 'e':
        continue
    print (s[i])
else:
    if i == 'd':
        print ('d is in the exact mid of the name')
    print ('ending')
##########################################################################################

n = 7

for i in range(0, n):
    for j in range (0, i+1):
        print ('+ ', end = '')
    print ('\r')


n = 7
for i in range (n, 0, -1):
    for j in range (n-i):
        print (' ', end = '')
    for j in range (2*i-1):
        print ('+ ', end = '')
    print ()
    print ('\r')

n = 7
for i in range (n, 0, -1):
    for j in range (n-i):
        print (' ', end = '')
    for j in range (i-1):
        print ('+ ', end = '')
    print ()
    print ('\r')


n = 7

for i in range(0, n):
    for j in range (0, i*2):
        print ('+ ', end = '')
    print ('\r')


n = 9
i = 0
while i < n:
    print ('* '*(i+1))
    i+=1

n = 9
i = 0
while i < n:
    print (' '*(n-i) , '* '*(i+1))
    i+=1

l1 = [3,5,2,5]
t1 = (4,5,6,2)

l1.pop(-2)

for i in range(len(l1)-1):
    print (l1[i])

for i in l1:
    if i%2 == 0:
        print (i)
    else:
        print ('odd numbers')


t1 = (4,5,6,2)

l2 = list(t1).insert(1,'to')


text1 = 'that\'s why'
text1.join('k')

for i in range (len(text1)):
    print (text1[i])

for i in range (len(text1)):
    print (text1[::-1])

# reversal without using ::-1
for i in range(len(text1)):
    print (text1[-i])   # 0 index will be there, which is t here
# or removing 0 as an index
for i in range(1, len(text1)):
    print (text1[-i])
# or
for i in range(len(text1)):
    print (text1[-i-1])
#============================================================================================
lst = [[[1,2]]]
for i in lst:
    for j in i:
        for k in j:
            print (k)
        print (j)
    print (i)
#============================================================================================  
# reversal using a while loop without ::-1
text1 = 'Hello'
ch = len(text1)-1
while ch >=0:
    print(text1[ch])
    ch = ch-1

text1.find('w')
for i in text1:
    print (text1.find('w'))
    break

# to find index of first name
name = 'what is my name, name repeating'
b = name.find('name')
for i in range(len('name')):
    print (b+i)

for i in reversed(name):
    print (i)
=================================================
a = 'we all are a Part of Data Science Program'
# question - print in lower letters
print (a.lower())

# question - print count of "a"
print (a.count('a'))
# or using for each loops
print(len([i for i in range(len(a)) if a[i] == 'a']))

# question - Replace a with python
print (a.replace('a', 'Python'))

# question. print all the words as a list
print (a.split())
# or 
print([i for i in a.split() ])

# question - Indexes where 'a' is present 
lst= []
for i in range(len(a)):
    if (a[i] == 'a'):
        lst.append(i)
print (lst)

# question - Indexes where 'a' is present # Second way
for i in range(len(a)):
    if (a[i] == 'a'):
        print (i)
        
# question - Indexes where 'a' is present # Third way
print([i for i in range(len(a)) if a[i] == 'a'])  



l1 = [1,2,3,['gh','t']]

# to pull nested list from list
for i in l1:
    if type(i) == list:
        print (i)
    else:
        print ('no list: ', i)


# len function vs own created function
a = 'This is a Python Class'

print (len(a))

count = 0
for i in a:
    count+=1
print (count)

# Identifying vowels from a string
name = 'Sandeep'
vow = 'AaEeIiOoUu'
for i in name:
    if i in vow:
        print (i, 'is a vowel')

    else:
        print ('not a vowel')
        
# print formatting, when we need some string data, then we use {}
'{} is my name'.format('Sandeep')
# for double values
'{} is {} name'.format('Sandeep', 'my')
# for triple values
'{} is {} {}'.format('Sandeep', 'my', 'name')
# we can give palce holder variable, which can be used to change variables place
'{a} is {b} {c}'.format(a = 'Sandeep', b = 'my', c = 'name')
print ('{a} is {b} {c}'.format(a = 'Sandeep', b = 'my', c = 'name'))



# entering an input
a = input('Enter your first name: ')
b = input('Enter your last name: ')
print('{} is my first and {} is my last name'.format(a,b))

# to check whether a word is a palindrom or not
# words, which can be written forward and backward direction have same meanings
# mom, nitin, arora, malayalam, xyx, 2002
a = input('Enter a word: ')
b = a[::-1]
if b == a:
    print ('its a palindrom')
else:
    print ('Not a palindrom')



#################
# to find location of second name in string
a = 'my name is name'
b = a.find('name')
c = b+len('name')
a.fin`d('name', c)

#============================================================================================
# Enumerate - Assign index to value
enumerate([1,2,3])  #wont show value, just shows type

# below code will work
for i in enumerate([1,2,3,4]):
    print (i)

# for string
str1 = 'hello'
print (enumerate(str1))     #wont show anything
# need to convert to list
list(enumerate(str1))
































