#######################################################################
#
#   Problem 2: Rotated Array Search (Solution)
#
#######################################################################

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
   
    return rotated_array_search_recursive(input_list, number, 0, len(input_list)-1)


def rotated_array_search_recursive(arr, number, left_index, right_index):
    '''
    Recursively search a subset of the arrays to find a target number
    '''

    # Check the left/right index for the answer
    if arr[left_index] == number:
        return left_index
    elif arr[right_index] == number:
        return right_index
        
    # Check for a null answer
    if right_index - left_index <= 1:
        return -1

    # Calculate the two array bounds
    mid_index = (left_index + right_index)//2

    # Case 1: Left is sorted
    if arr[left_index] < arr[mid_index]:
        if (arr[left_index] < number) and (number < arr[right_index]):
            return rotated_array_search_recursive(arr, number, left_index, mid_index)
        else:
            left_index = mid_index+1

    # Case 2: Right is sorted
    if arr[mid_index+1] < arr[right_index]:
        if (arr[mid_index+1] < number) and (number < arr[right_index]):
            return rotated_array_search_recursive(arr, number, mid_index+1, right_index)
        else:
            right_index = mid_index

    return rotated_array_search_recursive(arr, number, left_index, right_index)


#######################################################################
#
#   Problem 2: Rotated Array Search (Testing)
#
#######################################################################

# Test 1: Single pivot array with even length
arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
target = 6
output = rotated_array_search(arr, target)
print(output)
# Expected result = 0

# Test 2: Non-existent target value
arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
target = 5
output = rotated_array_search(arr, target)
print(output)
# Expected result = -1

# Test 3: Pivot index at end of array
arr = [2, 3, 4, 5, 6, 7, 8, 1]
target = 1
output = rotated_array_search(arr, target)
print(output)
# Expected result = 7

