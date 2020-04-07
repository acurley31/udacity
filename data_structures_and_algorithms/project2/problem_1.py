#######################################################################
#
#   Problem 1: Floored Square Root of a Number (Solution)
#
#######################################################################

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Case 1: number is its own square root
    if number*number == number:
        return number
    
    # Case 2: negative input (imaginary square root, return None)
    elif number < 0:
        return None

    # Case 3: Any other positive integer
    return sqrt_recursive(number, 0, number)


def sqrt_recursive(number, left, right):
    '''
    Recursively search for the floored square root of a number
    in the specified interval
    '''
    
    mid = (right + left)//2
    mid_squared = mid*mid
    lower_bound = (mid-1)*(mid-1)

    # Case 1: sqrt(number) = mid (answer found)
    if mid_squared == number:
        return mid

    # Case 2: sqrt(number) is in between the bounds (answer found)
    elif (lower_bound <= number) and (number <= mid_squared):
        return mid-1

    # Case 3: mid_squared > number
    elif mid_squared > number:
        right = mid

    # Case 4: mid_squared < number
    elif mid_squared < number:
        left = mid

    return sqrt_recursive(number, left, right)


#######################################################################
#
#   Problem 1: Floored Square Root of a Number (Solution)
#
#######################################################################

# Test 1: Simple low value square root
value = 16
output = sqrt(value)
print(output)
# Expected result = 4


# Test 2: Negative input value
value = -9
output = sqrt(value)
print(output)
# Expected result = None


# Test 3: Square root of a very large number
value = 912311233
output = sqrt(value)
print(output)
# Expected result = 30204


