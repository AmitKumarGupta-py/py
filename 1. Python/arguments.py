#
# #Default Arguments
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")
#
# # With Default Arguments
# greet("Alice")
# greet("Bob", "Hi")
# greet(name="Alice", message="Good morning")
# greet(message="Hi", name="Bob")


# #*args
# def add_numbers(*args):
#     return sum(args)
#
# # *args - Positional Arguments - With variable no of arguments
# print(add_numbers(1, 2, 3))
# print(add_numbers(5, 10, 15, 20))


#**kwargs with key value pair arguments
# def display_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# #

#**kwargs - with key value pair arguments
# display_info(name="Alice", age=30)
# display_info(city="New York", country="USA")



#With args and key value pairs both
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# With args and key value pairs both
display_info(1, 2, 3, name="Bob", age=25)



