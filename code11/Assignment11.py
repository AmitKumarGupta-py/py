def conversion():
	data1=float(input("Enter a unit of measurement in inches: "))
	num = int(input("Enter 1 to convert in feet, 2 to convert in meters or 3 to convert in centimeters: "))
	if num==1:
		print("inches in feet: ",data1/12,"feet")
		
	elif num==2:
		print("inches in meters: ",data1/39.37,"meters")
	elif num==3:
		print("inches in centimeters: ",data1/2.54,"centimeters")
			
	else:
		print("Enter a valid choice!")
while True:
	ch = input("enter the Y to convert inches into meters,feet,centimeters OR N to exit:   ")
	if ch == 'Y' or 'y':
		conversion()
	elif ch=='N' or 'n':
		break
	else:
		print("enter correct choices!")
	