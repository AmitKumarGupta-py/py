#empty list #it to create a empty list / tuple / dict /set before working on them 
list11= []
ch = int(input("enter the no. of element you wants in list: "))
for i in range(ch):
	x = input("enter the elements of list: ")


#inserting element in list using append() 
	list11.append(x)
print(list11)


#for i in list11:
	#accessing list elements using slicing
print(list11[0:])
print(list11[3]," ",list11[0])


#reversing the list using [::-1] negative indexing and slicing 
print(list11[::-1])

#adding an element in list using append()
list11.append(66)
print(list11)   



#converting a string into elements of list using split()
#split() split the string in which words are separated by spaces into individual words as element of list 
str1 = input("enter a string: ")
list12 = str1.split()
print(list12)

