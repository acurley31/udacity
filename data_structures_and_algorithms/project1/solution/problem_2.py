import os


#######################################################################
#
#   Problem 2: File Recursion
#
#######################################################################

def find_files(suffix, path):
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

    # Handle if the path is a file
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        return []

    # Check for a valid path
    if not os.path.exists(path):
        return []

    # Handle if the path is a directory
    matches = []
    subdirs = os.listdir(path)
    for subdir in subdirs:
        subdir_path = os.path.join(path, subdir)
        subdir_matches = find_files(suffix, subdir_path)
        for match in subdir_matches:
            matches.append(match)

    return matches


#######################################################################
#
#   Problem 2: File Recursion Test Cases
#
#######################################################################

# Test 1: Find all *.c files
test1_dir = './testdir'
test1_files = find_files('.c', test1_dir)
print(test1_files)
# Expected result = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']


# Test 2: Find non-existent file suffix
test2_dir = './testdir'
test2_files = find_files('.pkl', test2_dir)
print(test2_files)
# Expected result = []


# Test 3: Invalid input path (directory does not exist)
test3_dir = './my_missing_directory'
test3_files = find_files('.c', test3_dir)
print(test3_files)
# Expected result = []





