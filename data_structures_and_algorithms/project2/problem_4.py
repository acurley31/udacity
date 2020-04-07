#######################################################################
#
#   Problem 4: Sort 0, 1, 2 (Solution)
#
#######################################################################

def sort_012(arr):
    """
    Given an input input_list consisting on only 0, 1, and 2, sort the input_list in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    n = len(arr)
    next_0_index = 0
    next_2_index = n - 1
    front_index = 0

    while front_index <= next_2_index:
        if arr[front_index] == 0:
            arr[next_0_index], arr[front_index] = arr[front_index], arr[next_0_index]
            next_0_index += 1
            front_index += 1

        elif arr[front_index] == 2:
            arr[next_2_index], arr[front_index] = arr[front_index], arr[next_2_index]
            next_2_index -= 1

        else:
            front_index += 1

    return arr


#######################################################################
#
#   Problem 4: Sort 0, 1, 2 (Testing)
#
#######################################################################

# Test 1: Pre-sorted descending input (output should be reverse of input)
arr = [2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0]
output = sort_012(arr)
print(output)
# Expected result = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2]


# Test 2: 
arr = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
output = sort_012(arr)
print(output)
# Expected result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]


# Test 3: Pre-sorted ascending input (output should be the input)
arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
output = sort_012(arr)
print(output)
# Expected result = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]


