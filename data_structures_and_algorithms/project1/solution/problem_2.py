import os


#######################################################################
#
#   Problem 2: File Recursion Helper Classes
#
#######################################################################

class Node(object):
    '''Generic singly-linked node implementation'''

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    '''Generic singly linked list implementation'''

    def __init__(self):
        self.head = None
        self.number_of_elements = 0 

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.number_of_elements += 1
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = new_node
        self.number_of_elements += 1
 
    def pop(self, value):
        node = self.head
        if node.value == value:
            self.head = node.next
            self.number_of_elements -= 1
            del node
            return

        while node.next:
            if node.next.value == value:
                tmp = node.next
                node.next = node.next.next
                self.number_of_elements -= 1
                del tmp 
                return

    def size(self):
        return self.number_of_elements

    def is_empty(self):
        return self.size() == 0

    def to_array(self):
        items = [None for _ in range(self.number_of_elements)]
        node = self.head
        for i in range(self.number_of_elements):
            items[i] = node.value
            node = node.next

        return items

#######################################################################
#
#   Problem 2: File Recursion
#
#######################################################################

def find_files(suffix, path, matches=None):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # Initialize the matches linked list if necessary
    if matches is None:
        matches = LinkedList()

    # Handle if the path is a file
    if os.path.isfile(path):
        if path.endswith(suffix):
            matches.push(path)
            return matches
        return matches

    # Check for a valid path
    if not os.path.exists(path):
        return matches

    # Handle if the path is a directory
    subdirs = os.listdir(path)
    for subdir in subdirs:
        subdir_path = os.path.join(path, subdir)
        matches = find_files(suffix, subdir_path, matches)
        
    return matches


#######################################################################
#
#   Problem 2: File Recursion Test Cases
#
#######################################################################

# Test 1: Find all *.c files
test1_dir = './testdir'
test1_files = find_files('.c', test1_dir)
print(test1_files.to_array())
# Expected result = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']


# Test 2: Find non-existent file suffix
test2_dir = './testdir'
test2_files = find_files('.pkl', test2_dir)
print(test2_files.to_array())
# Expected result = []


# Test 3: Invalid input path (directory does not exist)
test3_dir = './my_missing_directory'
test3_files = find_files('.c', test3_dir)
print(test3_files.to_array())
# Expected result = []





