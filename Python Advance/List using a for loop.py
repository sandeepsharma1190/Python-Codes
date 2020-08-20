# Creating a list using a for loop

list1 = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter item at location", i, ":")
    item = input()
    list1.append(item)
print("User List is ", list1)

# for numbers
numberList = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)