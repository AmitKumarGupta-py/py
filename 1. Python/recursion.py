def recursive_sum(numbers):
    print(numbers)
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    else:
        # Recursive case: add the first number to the sum of the rest
        return numbers[0] + recursive_sum(numbers[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print("The sum of the list is:", result)

