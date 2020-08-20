def newfunc():
    yield 1
    yield 2
    yield 3
    yield 4

values = newfunc()

print (values.next())
print (values.next())

for item in newfunc():
    print (item)