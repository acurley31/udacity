# Problem 3: Rearrange Digits For Max Sum
**Algorith Design/Decisions**
* This task required the combination of digits in an array into two integers with the maximum sum in O(n log n) time
* The solution for this task can be broken down into two parts:
  1. Sorting the input array (performed with merge sort)
  2. Assembling the two largest integer values from the sorted array
* The data structures used in this solution were lists since the majority of this problem dealt with sorting the input list

**Time Complexity**
* The time complexity of this algorithm can be derived from its two parts:
  1. Merge sort O(n log n)
  2. Looping over the sorted array to assemble the two largest integers O(n)
* Combining these two time complexities, the result becomes O(n log n) + O(n) ~= O(n log n) since this term will dominate the expression for large n
