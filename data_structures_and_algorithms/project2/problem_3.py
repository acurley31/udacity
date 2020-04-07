#######################################################################
#
#   Problem 3: Rearrange Digits (Solution)
#
#######################################################################

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    input_sorted = mergesort(input_list)
    values = [0 for i in range(min(len(input_list), 2))]
    p = 0
    j = 0
    for i in range(len(input_list)):
        values[j] += input_sorted[i]*10**p
        if j == 0:
            j = 1
        else:
            p += 1
            j = 0

    return values


def mergesort(arr):
    '''Mergesort implementation to sort an array of numbers in ascending order'''
    
    if len(arr) <= 1:
        return arr

    mid_index = len(arr)//2
    left = arr[:mid_index]
    right = arr[mid_index:]
    
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    '''Merge two arrays together in acscending order'''

    left_index = 0
    right_index = 0 
    merged_index = 0
    merged = [None for _ in range(len(left) + len(right))]
    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] < right[right_index]:
            merged[merged_index] = left[left_index]
            left_index += 1
        else:
            merged[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    for i in range(left_index, len(left)):
        merged[merged_index] = left[i]
        merged_index += 1

    for i in range(right_index, len(right)):
        merged[merged_index] = right[i]
        merged_index += 1

    return merged


#######################################################################
#
#   Problem 3: Rearrange Digits (Testing)
#
#######################################################################

# Test 1: Even number of elements in input
arr = [1, 2, 3, 4, 5, 6]
output = rearrange_digits(arr)
print(output)
# Expected result = [531, 642]


# Test 2: Duplicate element
arr = [4, 7, 3, 0, 2, 3]
output = rearrange_digits(arr)
print(output)
# Expected result = [430, 732]


# Test 3: Empty array
arr = []
output = rearrange_digits(arr)
print(output)
# Expected result = []



