# Data Structures Rationale (Huffman Code)
**Date Structures Used:**
* Hash Map (used Python dictionary):
  * This structure was used briefly to efficiently store the character frequencies
  * An additional hash map was used to store the encoding key to allow for translation of the input string after tree construction
    * This was redundant as the input could have been translated while the codenames were generated/assigned to the tree nodes
* Priority Queue (implemented as a linked list):
  * To properly assemble the Huffman tree, the leaf nodes must be ordered according to their appearance frequency
  * For this reason, a simplified priority queue was used (essentially a linked list) in which items were inserted based on their specified priority (frequency)
* Tree (only partially implemented to accomplish the task):
  * Once all leaf nodes were added to the priority queue, the actual tree could be assembled
  * The tree was used such that the binary code associated with each character could function as the "directions" to the path


# Time/Space Complexity
**Time Complexity:**
* The implemenation of the encoding portion of the algorithm can be broken down into the following steps:
  1. Create a hash map of (characters, number of character occurrences) - O(n)
  2. Add each character to the priority queue
    * For this (inefficient) priority queue implementation, which inserts the element in the first possible properly ordered spot, it has a worst case time complexity of O(n log n) where n is the number of unique characters (in the worst case this is the length of the input). This case occurrs when the input items happen to be sorted in the reverse order of priority leading to insertion requiring (i.e. inefficient in-place sorting).
    * To improve the efficiency of this algorithm, two potential modifications to the priority queue implementation could be made:
      1. Implement the priority queue using a heap. This would be ideal and reduce the time complexity to O(log n) for both inserting and removing items.
      2. For a simpified solution, the priority queue insertion (enqueue) method could be changed to just append to the end [O(1)]. This would then make the dequeue method O(n) in the worst case scenario.
  3. The tree is assembled from the bottom up O(n) where n is the number of leaf nodes 
  4. With the completed tree, the encodings need to be set on the tree nodes which requires visiting every node. This was conducted using a depth-first search and is O(n)
  5. With the stored encodings hash map, translate the input to the encoded output O(n)
  6. As a result, the overall complexity of the encoding function is:
    * O(n) + O(n log n) + O(n) + O(n) + O(n) = O(5n + n log n)
    * In the worst case scenario, this expression is dominated by O(n log n) which becomes the simplified time complexity of encoding

* The implementation of the decoding portion of the algorithm can be broken down into the following steps:
  1. For each of the encoded characters, traverse the tree to find the corresponding character. In the worst case scenario, this would require O(n log n) time where n is the number of characters in the input.

**Space Complexity:**
* The implementation of the encoding portion of the algorithm requires the following space complexity:
  1. Frequencies hash map O(n) - can be discarded after the priority queue is assembled
  2. Priority queue/Tree O(n) - As the tree is assembled, the priority queue is disassembled. Together, they have a size of O(n) at any given time.
  3. Codec hash map O(n) - this is redundant and can be removed from this implementation
  4. The overall space complexity of the encoding is O(2n) which can be simplified to O(n)
* The implementation of the decoding portion of the algorithm requires O(k) space for the tree where k is the number of nodes in the tree and O(n) for the decoded input.
  * Together, these can be simplified to O(n) 

