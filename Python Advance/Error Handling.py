###### Error Handling #########
# Exception will remain on top
a = 5
b = 2
print (a/b) #--> it will work

a = 5
b = 0
print (a/b) #--> it wont work


# Through exceptipn
a = 5
b = 0
try:
    print (a/b)
except Exception:
    print ('You can not devide any figure with 0')
    
#== 2 way
a = 5
b = 0
try:
    print (a/b)
except Exception as e:
    print ('You can not devide any figure with 0:', e)

# 2 way 'Try, accept and finally'
# We use 'finally' when we need to put something in the end of output
# print ('Program closed') dont work in try and exception
    
a = 5
b = 0
try:
    print (a/b)
except Exception as e:
    print ('You can not devide any figure with 0:', e)
finally:
    print ('Program closed')

####Try and except#######
try:
    a = 2
    b = 0
    c = a/b
    print (c)
except ZeroDivisionError:
    print ('Number not divisible')

# inside a function
def divide_a_numb(n):
    return 5/n
print (divide_a_numb(0))  # ZeroDivisionError

# or
def divide_five_by_number(n):
    try:
        return 5 / n
    except:
        pass
print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))

# or
def divide_five_by_number(n):
    try:
        return 5 / n
    except ZeroDivisionError:
        return 'Cant divide fig with 0'
    except TypeError as t:
        return 'Cant divide fig with alphabet'
    
print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))

# or
def divide_five_by_number(n):
    try:
        return 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return 'Cant divide fig with 0'

print(divide_five_by_number("Nonsense"))
##########################################
####### IOError (Input-Output Error)######
  
try:
    string1 = open('SandeepFile')
    string1.write('Updated Text')
except IOError:
    print ('File doesn\'t exist')
else:
    print ('Program executed')

    
    
##########################################
############### Error name is not required, but its good pratice to know them ####################
try:
    string1 = open('SandeepFile')
    string1.write('Updated Text')
except:
    print ('File doesn\'t exist')
else:
    print ('Program executed')

##############################################################
try:
    fd = open('SandeepNewFile.txt', 'w')
    fd.write('Updated Text to add')
    fd.close()
except:
    print ('File doesn\'t exist')
else:
    print ('Program executed')
    
    
    
    
####################### TRY and Finally ######################################
try:
    newfn = open ('testfile.txt', 'w')
    try:
        newfn.write('This my file')
    finally:
        print ('Program executed and you got the result')
        newfn.close()
except IOError:
    print ('File doesn\'t exist')



































    