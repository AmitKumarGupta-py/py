###Reverse List by Swapping Present and Last Numbers at a Time


def list_reverse(arr, size):
    i = 0
    while i < size // 2:
        # swap elements from the start with elements from the end iteratively
        arr[i], arr[size - i - 1] = arr[size - i - 1], arr[i]
        i += 1
    return arr


arr = [1, 2, 3, 4, 5]
size = 5
print('Original list: ', arr)
print("Reversed list: ", list_reverse(arr, size))

### Reverse List Using the Reversed() and Reverse() Built-In Function
###Using reversed() 
###we can reverse the list and a list_reverseiterator object is created, 
###from which we can create a list using list() type casting. 
###Or, we can also use the list reverse() function to reverse list in place.

#Example 
lst = [10, 11, 12, 13, 14, 15]
print("Given list: ",lst)
lst.reverse() #reverse() make changes into the given list 
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst))) #reversed() reverse the list and need typecasting to create a new list  


###Reverse a List Using a Two-Pointer Approach

def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print("Given list: ",arr)
print("reversed list using 2 pointer approach: ",reverse_list(arr))


########### Reverse a List Using the insert() Function

#example []program behave like operation on stack i.e one element is poped from stack1 and pushed into stack2


# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)

###############
#Reverse a List Using List Comprehension

original_list = [10, 11, 12, 13, 14, 15]
new_list = [original_list[len(original_list) - i] for i in range(1, len(original_list)+1)]
print("Using list comprehension: ")
print(new_list)