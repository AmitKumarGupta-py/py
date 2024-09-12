#
# #Lambda function with a single parameter
# cube = lambda x:x*x*x
# print(cube(3))
# #------------------------------------------#
#
# str = 'tables'
# str_len = lambda str:len(str)
# print(str_len(str))
# #-------------------------------------#
# #
# #Can accept multiple variables
# iAdd = lambda x, y: x + y
# print(iAdd(5,3))
# #------------------------------------------#

#More complex application
# def custLambdaFunction():
#     return lambda val: val*val
#
# addNumbers = custLambdaFunction()
# print(addNumbers(4))
#
# #------------------------------------------#
# #
# def custLambdaFunction1(num):
#     return lambda val: val+num
#
# addValue = custLambdaFunction1(5)
# print(addValue(4))
#
# #------------------------------------------#
# #Higher order functions
# #------------------------------------------#
#
# # Example with map()
numbers = [1, 2, 3, 4, 10, 20, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
# #------------------------------------------#
#
# # Example with filter()
#
# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))
#
# #------------------------------------------#
#
# # Example with reduce()
#
# from functools import reduce
#
# sumNumbers = reduce(lambda x, y: x + y, numbers)
# print(sumNumbers)
#
#
