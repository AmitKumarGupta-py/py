#####Using insert() method adding elements to list 
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)

# Addition of Element at 
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
 
 
 ##Using extend() method
### extend(), this method is used to add """multiple elements at the same time""" at the """end of the list""".
"""Note: append() and extend() methods can only add elements at the end."""


# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)


####Removing Elements from the List

'''Using remove() method'''
# Remove() method only removes one element at a time, to remove a range of elements, the iterator is used.
##Note: Remove method in List will only remove the first occurrence of the searched element.

##The remove() method removes the specified item.


# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements(5,6): ")
print(List)

###Using pop() method


##pop() function can also be used to remove and return an element from the list, 
##but by default it removes only the last element of the list,
##to remove an element from a specific position of the List, 
##the index of the element is passed as an argument to the pop() method.

List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
