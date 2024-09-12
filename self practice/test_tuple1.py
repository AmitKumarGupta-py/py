'''str1 = input("Enter some no. separated by (,) : ")
print(str1)
str1 = str1.split()
print("\n\t",str1)

tupl1 = tuple(str1)
print("\n\t",tupl1)
tupl2 = tupl1[::-1]
print("\n\t",tupl2)
'''

"""name = input("enter name: ")
age = int(input("enter age: "))
tupl11 = ()
city = input("enter city name: ")
country = input("enter country name: ")
tupl11 = (city,country)
print(f"\n\tName:{name} Age: {age} City & Country: {tupl11}")

tupl12 = (name,age,tupl11)
print(tupl12)
'''upl22 = ()
for x in tupl12:
	tupl22.append(x)'''
#print("\n\n\t",tupl22)

tup34 = ()
Name,Age,tup34 = tupl12
print("\n\t",Name,"\t",Age,"\t",tup34)
tupl55 = ()
tupl55 = tupl12[::-1]
print("\n\t",tupl55)
print(len(tupl55))
count = 0
for x in tupl55:
	count+=1
print("count: ",count)

"""
n = ()
n = input("enter the no.: ")
#tup1 = tuple(n.split())
print("\n\n\t",n.split())
tup2 = ()
tup2 = sorted(n)
print("\n\n\t",tup2)
tup2 = tuple(tup2)
print("\n\n\t",tup2)
 