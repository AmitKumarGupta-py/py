def repeat_element():
    user_input = input("Enter a tuple of elements (separated by commas): ")

    original_tuple = tuple(user_input.split(","))

    element_to_repeat = input("Enter an element to repeat: ")
    repeat_count = int(input("Enter the number of times to repeat: "))

    new_tuple = []
    for element in original_tuple:
        if element == element_to_repeat:
            new_tuple.extend([element] * repeat_count)
        else:
            new_tuple.append(element)

    print("Original Tuple:", original_tuple)
    print("New Tuple:", tuple(new_tuple))

repeat_element()