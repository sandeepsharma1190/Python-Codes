# Leap year programs

year=int(input("Enter any year : "))
if (year%4)==0:
    print ("it is a leap year")
else:
    print ("it is not a leap year")
    
# leap year program using while true (not to use):
year=int(input("Enter any year : "))
while True:
    if (year %4)==0:
        break
print ("It is a leap year")      
