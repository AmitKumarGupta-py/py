x =  int(input("Enter a num to find the its factorial "))
count = 1
if x == 0:
	print("factorial ",1)
elif x == 1:
	print("factorial ",1)
else :
	fact = 1
	while count <= x:
		fact = fact * count
		count+=1
	print("fact ",fact)