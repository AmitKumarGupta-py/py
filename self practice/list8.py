"""---------------------------------------------------"""
# Convert the Given List into Nested List in Python
"""================================================"""

# Below are the ways by which we can convert a given list into a Nested List in Python:

# Using iteration
# Using a list with numeric values 
# Using map(), split() and lambda
# Using list comprehension
# Using numpy library
# Using heapq

"""-----------------------------------------"""
# Convert the Given List into Nested List Using Iteration

# List initialization
Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']
 
temp = []
 
# Getting elem in list of list format
for elem in Input:
	temp2 = elem.split(', ')
	print(temp2)
	temp.append((temp2))

# List initialization
Output = []
 
for elem in temp:
    temp3 = []
    for elem2 in elem:
        temp3.append(elem2)
    Output.append(temp3)
 
# printing
print(Output)

"""======================================================="""
#Python Convert List into Nested List Using List With Numeric Values
"""=================================================================="""
#In this example, the Python code utilizes the """ast.literal_eval""" function 
#to safely convert a list of comma-separated string elements (Input) into a list of lists (Output) containing numerical values,
# demonstrating an approach that ensures proper evaluation and avoids potential security risks.


# importing
import ast
 
# List Initialization
Input = ['12, 454', '15.72, 82.85', '52.236, 25256', '95.9492, 72.906']
 
# using ast to convert
Output = [list(ast.literal_eval(x)) for x in Input]
 
# printing
print(Output)


##########################################################

"""Convert Python List into Nested List Using map(), split() and lambda"""
# initializing list of strings
Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']
 
Output = list(map(lambda x: x.split(', '), Input))
print("Result: "+str(Output))

##
#Turning a List into Nested Lists in Python Using List Comprehension

# List initialization
Input = ['Geeeks, Forgeeks', '65.7492, 62.5405',
         'Geeks, 123', '555.7492, 152.5406']
 
# Using list comprehension to convert
# element into list of list
output = [elem.split(', ') for elem in Input]
 
# printing
print(output)


"""#####################################"""

#Python Nested List to Single Value Tuple

#Below are the ways by which we can convert nested lists to single-value tuples:

"""
	Using list comprehension ( For single nesting )
	Using isinstance() + recursion
	Using extend() method
	Using Two nested loop
	Using map and chain functions
	Using reduce() function and add operator
	Using NumPy
"""

#Flatten Nested List to Single-Value Tuples with List Comprehension

# initializing list
test_list = [[5, 6], [4, 7, 10], [12], [9, 11]]

# printing original list
print("\nThe original list is : " + str(test_list))

# Convert Nested List to 1 value Tuple
# Using list comprehension
res = [(ele,) for sub in test_list for ele in sub]

# printing result
print("\nThe converted container : " + str(res))


"""================================================="""
