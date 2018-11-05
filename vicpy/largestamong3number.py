num1=int(input("enter first number"))
num2=int(input("enter second  number"))
num3=int(input("enter third number"))

if(num1>num2):
	if(num1>num3):
		print("the lagest is ",num1)
	else:
		print("the lagest is ",num2)
elif(num2>num3):
	print("the lagest is ",num2)
else:
	print("the lagest is ",num3)