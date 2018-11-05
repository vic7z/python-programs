n=int(input("enter a number"))
cp=n
rev=0
sum=0
while(n>0):
	rev=n%10
	sum+=rev**3
	n=n//10
if(cp==sum):
	print("the given no is amstrong ")
else:
	print("the given no is not amstrong ")