def vol(a):
	an=["a","e","i","o","u","A","E","I","O"]
	for s in a:
		if s in an:
			return 1
		else:
			return 0

a=raw_input("enter a string  \t:")
if (vol(a)):
	print("the string contain vowel")
else:
	print("the string does not contain vowel")