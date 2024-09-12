# print("enter your choice 1. Add 2. Sub 3. Multiplication 4. Division")
# ch = int(input())
# a = float(input("enter values a : "))
# b = float(input("enter values b : "))
while True:
	print("enter your choice 1. Add 2. Sub 3. Multiplication 4. Division")
	ch = int(input())
	a = float(input("enter values a : "))
	b = float(input("enter values b : "))
	
	if ch == 1:
		print("sum: ",a+b)
	elif ch == 2:
		print("subStraction: ",a-b)
	elif ch == 3:
		print("Multiplication= ",a*b)
	elif ch == 4:
		print("Division= ",a/b)
	else:
		print("Invalid Choice")
	opt = input("Wants to continue: 'y' or 'n'  " )
	if opt.lower() != 'y':
		break

