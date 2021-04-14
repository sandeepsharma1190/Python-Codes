# iterator - How for loop works

# we can iterate below mention code, hence we can call it is as an iterable object not as iterators
# List and tuples are iterable objects as well
# basically we write code to iterate through strings and all
txt = [1,3,4]
for i in txt:
    print (i)

# next command shows us whether a value is an iterator or not
# next picks next value from data
next ([2,3],[3,4])

# iter means iterator
a = iter('sandeep')
type(a)

# to pull all characters one by one
next(a) # it will show different value
# in first run, it will show 's', than 'a' until 'p'

for i in a:
    print (next(a))














