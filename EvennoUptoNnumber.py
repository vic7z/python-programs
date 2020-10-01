n =int(input("enter limit")) 	#input
if(n>0):
	for i in range(n):   					#for loop
		if(i%2==0):     					#even or not checking
			print(i)
else:
	print("Number should be an integer number greater than 0")
