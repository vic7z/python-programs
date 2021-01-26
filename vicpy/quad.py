import math
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
s1,s2=0,0
if a=0:
    print("Value of a should not be 0")
    break
else:
    s1=-b+math.sqrt((b**2)-4*a*c)
    print(s1/2*a)
    s2=-b-math.sqrt((b**2)-4*a*c)
    print(s2/2*a)
