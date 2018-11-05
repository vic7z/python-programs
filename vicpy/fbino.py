n1=int(input("enter a limit"))
p=0
c=1
n=0
print(p)
print(c)
for i in range(2,n1):
	n=p+c
	p,c=c,n
	print(n)
