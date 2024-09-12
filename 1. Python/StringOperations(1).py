#
# single_quotes = 'Hi there single quotes'
# double_quotes = "Hi there double quotes"
# triple_quotes = '''Hi there triple quotes'''
#
# # print(type(single_quotes))
# # print(double_quotes)
# # print(triple_quotes)
#
# #
# # escape_sequence = 'hi weather is \'good\'!\n have a good day!!'
# # print(escape_sequence)
#
# # # String operations
# # # str1 = abc
# # # str2 = def
#
# str1 = "Quick brown fox"
# str2 = " jumps over lazy dog"
#
# # ---------------------------------------------------#
# # Concatenation
# result = str1 + str2
# # print ("Concatenated strings are: ",result)
# # ---------------------------------------------------#
# # # Repetition - repeat concatenated string thrice
# repititionResult = result * 3
# print("Repeated strings are : ",repititionResult)
# # # ---------------------------------------------------#
# # # Indexing
# firstChar = result[0]
# lastChar = result[-1]
# secondChar = result[1]
# print(firstChar)
# print(lastChar)
# print(secondChar)
# # # ---------------------------------------------------#
# # Slicing
# substring = repititionResult[0:7]
# print(substring)
# # # ---------------------------------------------------#
# # # Length Calculation
# length = len(result)
# print("Length of string is : ",length)
# # # ---------------------------------------------------#
# # String Membership
result = "ahfajdfasdj"
member = "abc" in result
print(member)
#
# # ---------------------------------------------------#
# # String Comparison
str1 = "asdasdasd"
str2 = "asdasdasd"
resultCompare = str1 == str2
print(resultCompare)
#
# # ---------------------------------------------------#
# # Case Conversion
#
print(result.lower())
print(result.upper())
print(result.title())

# # ---------------------------------------------------#
# # Strip (Trimming Whitespace)
resultWhitespace = str1 + ' ' + str2
print("With WhiteSpace",resultWhitespace)

stripped_string = resultWhitespace.strip()
print("Without Whitespace",stripped_string)

# # ---------------------------------------------------#
# # Find and Replace
#
position = result.find("abc")
new_string = result.replace("abc", "ABC")
print(position)
print(new_string)

# # ---------------------------------------------------#
# # Splitting
#
resConcatenate = str1 + ',' + str2
resSplit = resConcatenate.split(",")
print(resSplit)

# # ---------------------------------------------------#
# # Joining
#
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)
#
# # ---------------------------------------------------#
# # String Formatting
#
name = "Alice"
age = 25
# Using format() method
result = "My name is {} and I am {} years old.".format(name, age)
# Using f-string
result_f = f"My name is {name} and I am {age} years old."
print(result)   # Output: "My name is Alice and I am 25 years old."
print(result_f)
#
