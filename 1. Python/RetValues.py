#
# def calculate_area(length, width):
#     area = length * width
#     return area
#
# #Single return value
# ret_area = calculate_area(5.1, 3)
# print(type(ret_area))

#
# def calculate_area_and_perimeter(length, width):
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter
# #
#
# # Multiple return values
# ret_val = calculate_area_and_perimeter(5, 3)
# print(type(ret_val))
#
# #unpacking tuple of returned values
# area, perimeter = calculate_area_and_perimeter(5, 3)
# print("Area:", area)
# print("Perimeter:", perimeter)

def noRetVal():
    print("in func noRetVal")

#No return value
val = noRetVal()
print(type(val))
print(type(noRetVal()))