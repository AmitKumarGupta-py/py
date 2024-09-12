
dict = {'a':1,'b':2,'c':3,'d':4}
print (dict)

print (dict['c'])
print(dict.get('c'))

# Values that a dict can take
my_dict = {
    "integer_value": 42,
    "string_value": "This is a string",
    "tuple_value": (1, 2, 3),
    "list_value": ["a", "list", "of", "strings"],
    "nested_dict": {"key1": "value1", "key2": 2}
}
#
print (my_dict)
print (my_dict['list_value'])


# Removing Entries
a = dict.pop('a')
print(a)
#
del dict['c']
print(dict)

# Checking for Keys
if 'abc' in dict:
    print("b is present")

# Iterating Over a Dictionary

for key in dict:
    print(key)

# Iterating over values
for value in dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in dict.items():
    print(f"{key}: {value}")

# Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
#
# # Using update() method
dict1.update(dict2)
print(dict2)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using dictionary unpacking (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(merged_dict)


# Clearing dictionaries
dict.clear()
print(dict)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)
