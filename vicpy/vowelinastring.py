def vol(a):
	an=["a","e","i","o","u","A","E","I","O"]
	for s in a:
		if s in an:
			print(s)

q=raw_input("enter a string  \t:")
vol(q)