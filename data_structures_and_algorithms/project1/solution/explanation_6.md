# Data Structures Rationale (Union and Intersection of Two Linked Lists)
**Data Structures Used:**
* By default, the data structure used in this exercise is a singly linked list
* Hash map
  * To eliminate the duplication of items in the intersections/unions, a hash map was selected for fast insertion and retrieval of records

# Space/Time Complexity
**Time Complexity:**
* For calculating the intersection of two linked lists, the time complexity is O(n*m) where n is the number of elements in the first list and m is the number of elements in the second list
  * This is due to every node in the first list needing to be checked against (potentially) all nodes in the second list
* For calculating the union of two linked lists, the time complexity is O(n + m) where n is the number of elements in the first list and m is the number of elements in the second list
  * This is due to needing to loop through both lists independently and adding their respective values to a combined list
  
**Space Complexity:**
* For both the intersection and union operations, the following space complexity for this implenentation is:
  * Linked list 1 O(n)
  * Linked list 2 O(m)
  * Resulting linked list O(n + m)
  * Used value hash map O(n + m)
* The resulting space complexity is O(2n + 2m) which can be simplified to O(n + m)
