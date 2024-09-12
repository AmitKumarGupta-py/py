#
#
# # Creating a List
# #
my_list = [5, 6, 1, 7, 9,0]
print(my_list)
# # empty_list = []
# # print(empty_list)
# # mixed_list = [1, "hello", 3.14, True]
# # print(mixed_list)
#
#
# # Accessing Elements
# print(my_list)
# # first_element = my_list[0]
# # last_element = my_list[-1]
# # print(first_element)
# # print(last_element)
#
# # # Slicing
# # sub_list = my_list[1:3]
# # print(sub_list)
#
# # # Modifying Elements
# my_list[0] = 10
# print(my_list)

# # Adding Elements
# my_list.append(6)  # Adds 6 at the end
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
#
# my_list.insert(1, 15)  # Inserts 15 at index 1
# print(my_list)  # Output: [1, 15, 2, 3, 4, 5]
#
# my_list.extend([7, 8, 9])  # Extends the list by adding elements from another list
# print(my_list)

#
# # Removing Elements
# del my_list[0]  # Deletes the element at index 0
# print(my_list)
#
# removed_element = my_list.pop(1)  # Removes and returns the element at index 1
# print(removed_element)  # Output: 2
# print(my_list)  # Output: [1, 4, 5]
#
# my_list.remove(5)  # Removes the first occurrence of 3
# print(my_list)  # Output: [1, 2, 4, 5]
#
# # Finding index of Elements
# print("Finding index of Elements")
# print(my_list)
# index_of_four = my_list.index(4)
# print(index_of_four)  # Output: 0

# # #Find no of occurences
# count_of_five = my_list.count(5)
# print(count_of_five)

# Sorting a List
# my_list = [5, 2, 9, 1]
# my_list.sort()
# print(my_list)  # Output: [1, 2, 5, 9]

# my_list_sorted = sorted(my_list, reverse=True)
# print(my_list_sorted)
#
# #Reversing a List
# my_list.reverse()
# print(my_list)
#
# # Copying a List
# my_list_copy = my_list.copy()
# print(my_list_copy)
#
# another_copy = my_list[:]
# print(another_copy)

# # Clearing a List
# my_list.clear()
# print(my_list)

# Joining Lists
# list1 = [1, 2, 3]
# list2 = [4, 5]
# combined_list = list1 + list2
# print(combined_list)

# # Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)
print(nested_list[0][0])

#
#
#


#
# # List Comprehensions
# squares = [x**2 for x in range(1, 6)]
# print(squares)