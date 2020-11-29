def fibino(n1):
	if(n1<=1):
		return n1
	else:
		return(fibino(n1-1)+fibino(n1-2))

n1=int(input("enter a limit"))
for i in range(2):
	print(fibino(i))