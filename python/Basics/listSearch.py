mylist=[]

a=int(input("enter the no of elements"))

for i in range(a):
    mylist.append(int(input("enter a value")))


c=int(input("enter the value to be searched"))


if c in mylist:
    print("item found")
else:
    print("item not found")