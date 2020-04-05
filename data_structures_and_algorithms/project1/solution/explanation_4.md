# Data Structures Rationale (Active Directory)
**Data Structures Used:**
* To determine if a user exists in a group in active directory, a tree was used to represent the parent/child relationship of groups and their associated subgroups and users

# Time/Space Complexity
**Time Complexity:**
* The time complexity of checking if a user exists in a group is O(n) in the worst case scenario. This is due to each leaf nodes potentially having to be checked against the specified user.

**Space Complexity:**
* The space complexity of the active directory user permission check is O(n) where n is the number of nodes in the tree (i.e. the cumulative number of groups/user combinations)
