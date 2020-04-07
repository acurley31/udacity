# Problem 2: Rotated Array Search
**Algorithm Design/Decisions**
* This task was to search a singly-pivoted array to find a target value (if it exists) in O(log n) time
* The solution algorithm for this task exploited the pre-sorted characteristic of subarrays in order to recursively reduce the search pool
* For this algorithm, the main data structure was an array (the input). No other data structures were needed.

**Time Complexity (Worst Case)**
* The time complexity of this solution is O(log n) since the search pool is n/2 for each subsequent search

**Space Complexity**
* The space complexity of this solution is O(1) since it is an in-place sorting method
