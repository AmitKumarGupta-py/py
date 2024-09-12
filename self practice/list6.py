
#lists as element of a list

matrix = []
for i in range(5):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

##without list comprehension
##Flattening Nested Sub-Lists
# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
 
flatten_matrix = []
 
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
 
print(flatten_matrix)


###With List Comprehension

# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
 
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
 
print(flatten_matrix)


#### Manipulate String Using List Comprehension
###  Without List Comprehension

matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]
 
modified_matrix = []
for row in matrix:
    modified_row = []
    for fruit in row:
        modified_row.append(fruit.capitalize())
    modified_matrix.append(modified_row)
 
print(modified_matrix)


##With List Comprehension

matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]
 
modified_matrix = [[fruit.capitalize() for fruit in row] for row in matrix]
 
print(modified_matrix)
