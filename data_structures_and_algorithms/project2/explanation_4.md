# Problem 4 (Dutch National Flag)
**Algorithm Design/Decisions**
* This task was to sort an array consisting solely of 0's, 1's, 2's in a single traversal
* The solution algorithm for this task exploited the fact that there were only three possible "buckets" for a value to be in
  * As such, any 0 will be put in the front bucket and any 2 will be put in the rear bucket
  * With this in mind, indices tracking the tail of the lead bucket and the start of the rear bucket were followed and updated throughout the single traversal
* This was an in-place sorting procedure with the data structure of the input being an array

**Time Complexity**
* The time complexity of this algorithm is O(n) since it requires only a single pass over the input array

**Space Complexity**
* The space complexity of this algorithm is O(n) since it is an in-place sorting procedure
