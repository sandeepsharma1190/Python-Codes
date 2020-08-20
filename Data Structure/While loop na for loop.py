'''While loop (infinite loop)'''

i = 1
while i < 5:
    print (i)
    i = i+1

'''Break is used as control statement, as soon as it is 
encountered the execution, skips the rest of the coding'''
x = 1
while x <= 5:
    print (x)
    if x == 3:
        break
    x = x+1
    

'''Break is used as control statement, as soon as it is 
encountered the the current iteraton is akipped.'''
x = 1
while x <= 5:
    if x == 3:
        x=x+1
        continue
    else:
        print (x)
        x = x+1

i = 1
while i < 10:
    print (i)
    i+=1
    
i = 1
j = 5
while i < 6:
    while j > 0:
        print (i, j)
        i = i+1
        j = j-1
    
    
    
