# Logging

import logging as lg
lg.basicConfig(filename = 'C:\\Users\\sshar127\\testing1\\test_new1.log', level = lg.INFO)
def test2(a,b):
    lg.info('Just a starting')
    return a+b

test2(4,4)


# fkjfpisj
# to do 

import logging as lg

def test1(*n):
    lg.basicConfig(filename = 'C:\\Users\\sshar127\\testing1\\test_new2.log', level = lg.INFO, format = '%(asctime)s - %(message)s' )
    lg.info('We will add your data')
    lg.info(n)
    return sum(n)

test1(1,2,3,4,5)

infile = r'C:\Users\sshar127\testing1\test_new2.log'

with open(infile) as f:
    f = f.readlines()
    print (f)








