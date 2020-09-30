n =int(input("enter limit")) 	#input
if (n>0):
	for i in range(n):   					#for loop
		if(i%2==0):     					#even or not checking
			print(i)
else:
	print("Limit should be a natural number")
