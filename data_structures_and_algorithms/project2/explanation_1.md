# Problem 1: Floored Square Root
**Algorithm Decisions/Design**
* This task required the calculation of the floored square root in O(log n) time which suggested a recursive approach to narrow down the solution
  * Note: the solution essentially implements a binary search on calculated value at each step
* The basic idea of the algorithm is to recursively narrow an interval of all potential solutions by halving the previous result
* For this task, only primitive data types were needed (integers)

**Time Complexity (Worst Case)**
* The time complexity of this algorithm is O(log n) since the search interval is at most n/2 for each subsequent step

**Space Complexity**
* The space complexity of this algorithm is O(1) as only a handful of calculated values are used throughout
