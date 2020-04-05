# Data Structures Rationale (File Recursion)
**Data Structures Used:**
* The premise of this problem is coninuously search and find files that match the specified suffix. Naturally, this requires efficient insertion into a data structure knowing that the order of the elements does not matter.
* For fast insertion, a singly-linked list was implemented with a method to convert to an array (mostly for printing operations in this case, but could be used for integration into an existing system)

# Time/Space Complexity
**Time Complexity:**
* The time complexity of file recursion is dependent on the number of child directories and files as each item needs to visited and checked against the target suffix
* As a result this algorithm is O(n) where n is the number of child directories and files

**Space Complexity**
* In the worst case scenario, the space complexity of this algorithm is O(n) assuming that every child item matched the target suffix
