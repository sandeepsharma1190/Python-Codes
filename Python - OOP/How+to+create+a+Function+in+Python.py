def rectangle_area(width, length):
           area = width * length 
           return area
rectangle_area(6, 9)

rectangle_area(4, 15)


def is_even(x):
    if x % 2 == 0:
        return True
    else:       
        return False

is_even(10)


def is_odd(y):
    if y % 2 == 0:
        return True
    else:       
        return False 
is_odd(8)

def countdown(x):
    while x> 0:
        print(x)
        x = x-1
        print("Stop this is the end!")
        
countdown(2)


def is_even_or_odd(x):
    if x % 2 == 0:
        return "this number is even"
    else:
        return "this number is odd"
is_even_or_odd(2)

is_even_or_odd(7)



