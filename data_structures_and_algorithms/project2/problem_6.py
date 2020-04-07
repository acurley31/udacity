#######################################################################
#
#   Problem 6: Min/Max of an unsorted list of integers (Solution)
#
#######################################################################

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    min_value = ints[0]
    max_value = ints[0]
    for i in range(1, len(ints)):
        if ints[i] < min_value:
            min_value = ints[i]
        if ints[i] > max_value:
            max_value = ints[i]
        
    return (min_value, max_value)

#######################################################################
#
#   Problem 6: Min/Max of an unsorted list of integers (Solution)
#
#######################################################################

# Test 1: Sorted ascending input
arr = [0, 1, 2, 3, 4, 5, 6]
output = get_min_max(arr)
print(output)
# Expected result = [0, 6]


# Test 2: Unsorted input
arr = [9, 5, 1, 6, 7, 2, 4]
output = get_min_max(arr)
print(output)
# Expected result = [1, 9]


# Test 3: Negative and positive inputs
arr = [0, 4, 10, -23, 4, 1, 8]
output = get_min_max(arr)
print(output)
# Expected result = [-23, 10]


