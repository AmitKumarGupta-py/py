# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)

# # Creating a set with the set() function
another_set = set([1, 2, 3, 4, 5])
print(another_set)

#Set can contain multiple datatypes
mult_set = {1,2,'stanother_setring',12.4}
print(mult_set)

#iterating over a set
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)

# Checking membership in a set
if 6 in my_set:
    print("'1' is in the set.")
else:
    print("'6' is not in the set.")

#Adding Elements
my_set.add(6)  # Adds 6 to the set
print(my_set)

#Removing Elements
print (my_set)
my_set.remove(3)
my_set.discard(5)
print (my_set)
#
# #Set Union
set1 = {10, 2, 3}
set2 = {3, 4, 7, 3}
union_set = set1.union(set2)
print("Set Union", union_set)

#Set Intersection
intersection_set = set1.intersection(set2)
intersection_set = set1 & set2
print("Set Intersection",intersection_set)

#Set Difference
print(set1)
print(set2)
difference_set = set2.difference(set1)
print("Set Difference",difference_set)
print("Set Symmetric Difference",set1.symmetric_difference(set2))


#Removing duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
print(my_list)
unique_elements = set(my_list)
print(unique_elements)  # Output: {1, 2, 3, 4, 5}

#accessing a single element in a set gives an error
###my_set[0]

#converting set to List
my_set = {5, 2, 3, 1, 4}
ordered_list = sorted(my_set)
print(ordered_list)
