#Break Continue Pass

# Break
av = 5
x = int(input('Enter no. of items: '))
i = 1
while i <= x:
    if i >av:
        print('Out of stock')
        break
    print ('Candy', i)
    i +=1
    
# Continue
for i in range (1,101):
    if i%3 == 0:
        continue
    print (i)
# or
for i in range (1,101):
    if i%3 == 0 or i%5 ==0:
        continue
    print (i)

#or (all values will be remove which is divisible by 3, 5 or 7 sepratly)
for i in range (1,101):
    if i%3 == 0 or i%5 ==0 or i%7 == 0:
        continue
    print (i)  
    
# using and with continue
# and (all values will be remove which is divisible by 3 and 5 together)
for i in range (1,101):
    if i%3 == 0 and i%5 ==0:
        continue
    print (i)    
    
# Pass
for i in range (1,101):
    if (i%2 != 0):
        pass
    else:
        print (i)
    
    
    
    
    
    
    
    
    
    
    