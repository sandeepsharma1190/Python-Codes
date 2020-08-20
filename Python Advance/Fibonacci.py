# Fibonacci series
# 1,1,2,3,5,8.................n
# 1, 1+1 = 2, 2+1 = 3, 3+2 = 5 ............ n

def fib (n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fib (n-1) + fib (n-2)
    
for n in range (1,11):
    print (n, ':', fib(n))
    
# if we will use (1, 100) it will get slow down, need to fix spped we use memoization
# it will clear cache values    
# Fibonacci series
i = 1
x = 1
y = 2
while i <= 100:
    print (x, end = ' ')
    nextterm = x+y
    x = y
    y = nextterm
    i = i+1
    
# Python Fibonacci series Program using For Loop

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("Please Enter the Range Number: "))
# Initializing First and Second Values of a Series
First_Value = 0
Second_Value = 1
# Find & Displaying Fibonacci series
for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)