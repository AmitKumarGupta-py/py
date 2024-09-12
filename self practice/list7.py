# Test for Nested List in Python
# Below are the ways by which we can test for nested lists:

# Using any() and instance()
# Using type() Method
# Using recursive function

## Test for Nested List Using any() and instance()

# initialize list
test_list = [[5, 6], 6, [7], 8, 10]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Test for nested list
# using any() + isinstance()
res = any(isinstance(sub, list) for sub in test_list)
 
# printing result
print("Does list contain nested list ? : " + str(res))
"""
   The any() is used to check for each of the occurrences and
   the isinstance() is used to check for the list. 
"""

"""########################"""

# Python Test Nested List Using type() method

# initialize list
test_list = [[5, 6], 6, [7], 8, 10]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Test for nested list
res=False
for i in test_list:
    if type(i) is list:
        res=True
        break
# printing result
print("Does list contain nested list ? : " + str(res))


"""##########"""

#Testing for Nested List Using Recursive Function

def has_nested_list(lst):
    for elem in lst:
        if isinstance(elem, list):
            return True
        elif isinstance(elem, (tuple, set)):
            # check nested tuples and sets too
            if has_nested_list(list(elem)):
                return True
    return False
 
# Example usage
lst = [[5, 6], 6, [7], 8, 10]
result = has_nested_list(lst)
print(result)  # Output: True



"""========================================"""


# Copy a Nested List in Python
# Below are the ways by which we can copy a nested list in Python:

# Using Iteration 
# Using deepcopy 
# Using list comprehension and slicing 
# Using the json module

#Copy a Nested List Using Iteration

# the code iterates through a nested list (Input_list)
 # using nested loops to create a new list (Output). 
# The inner loop assigns values to a temporary list,
 # which is then appended to the outer list, 
# resulting in a copy of the structure of the original nested list.

# List initialization
Input_list = [[0, 1, 2], [3, 4, 5]]
Output = []
 
# Using iteration to assign values
for x in range(len(Input_list)):
    temp = []
    for elem in Input_list[x]:
        temp.append(elem)
    Output.append(temp)
 
# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(Output)

"""#####################"""

#Python Copy a Nested List Using Deepcopy
"""a nested list Input is duplicated to Output using copy.deepcopy() 
to ensure an independent copy of both the outer and inner list elements. 
The program then prints the initial and newly assigned lists for verification."""
# Python program to copy a nested list
import copy
 
# List initialization
Input = [[1, 0, 1], [1, 0, 1]]
 
# using deepcopy
Output = copy.deepcopy(Input)
 
# Printing
print("Initial list is:")
print(Input)
print("New assigned list is")
print(Output)


"""================"""
#Copy a Nested List Using List Comprehension and Slicing

# List initialization
Input_list = [[0, 1, 2], [3, 4, 5], [0, 1, 8]]
 
# comprehensive method
out_list = [ele[:] for ele in Input_list]
 
# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(out_list)



"""**********************************************************"""
# How to Copy a Nested List Using the Json Module
"""----------------------------------------------------"""
# The json module can be used to serialize and deserialize data in JSON format.
 # This means that you can convert the nested list to a JSON string, and then parse the string to create a new list. 
# This method can be useful if the elements in the nested list are serializable, 
# but may not be suitable if the elements are not serializable."""

import json
 
# List initialization
Input_list = [[0, 1, 2], [3, 4, 5]]
 
# Convert the list to a JSON string
json_str = json.dumps(Input_list)
 
# Parse the JSON string to create a new list
Output = json.loads(json_str)
 
# Printing Output
print("Initial list is:")
print(Input_list)
print("New assigned list is")
print(Output)