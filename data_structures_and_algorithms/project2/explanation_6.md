# Problem 6: Max/Min of Unsorted Integer Array
**Algorithm Design/Decisions**
* This task was to retrieve the min and max values of an integer array in O(n) time
* Since the input data structure of this task was an array and the output was an array, only arrays were needed outside of primitives

**Time Complexity (All Cases)**
* The time complexity of this algorithm is O(n) since the input array needs to be traversed only once with two comparisons per element
  * Throughout the traversal, each element is compared against the existing min and max values and updated accordingly
  
**Space Complexity**
* The space complexity of this algorithm is O(1) since only two other primitives are needed.
