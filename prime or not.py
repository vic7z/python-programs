num=int(input("enter a no:"))
if(num>1):
	for i in range(1,num):
		if(num%i==0):
			print("not a prime no")
			break
		else:
			print("prime no")
else:
	print("not a prime")