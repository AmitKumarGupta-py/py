#############    MAP()   #################


# input size of the list
n = int(input("Enter the size of list : "))

# store integers in a list using map,
# split and strip functions
#list()used to convert the strings into list
lst = list(map(int, input("Enter the integer elements:").strip().split()))[:n]
#strip() remove the white spaces 

# printing the list
print('The list is:', lst)


#map() function returns a map object(which is an iterator) of the results
#after applying the given function to each item of a given
#iterable (list, tuple etc.)

"""Python map() Function Syntax
Syntax : map(fun, iter)

Parameters:

	fun: It is a function to which map passes each element of given iterable.
	iter: It is iterable which is to be mapped.

NOTE: You can pass one or more iterable to the map() function.

Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) ."""



###Example1 of Map()

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
print("#",numbers,"#")
#here fuction NAME is passed as parameters for map and numbers is a list
result = map(addition, numbers)
print("$",list(result),"$")



#####map() with Lambda Expressions

###We can also use lambda expressions with map to achieve above result. 
###In this example, we are using map() with lambda expression.

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
"""lambda""" #is a anonymous fuction without a name 

print("%",list(result),"%")


#######################################
"""   Python Lambda Function Syntax"""
# Syntax: lambda arguments : expression

#1: this function can have any number of arguments but only one expression, which is evaluated and returned.
#2: One is free to use lambda functions wherever function objects are required.
#3: You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
#4: It has various uses in particular fields of programming, besides other types of expressions in functions."""

## Exaple of lambda fuction
str1 = 'GeeksforGeeks'

upper = lambda string: string.upper()
print(upper(str1))