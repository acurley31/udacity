# Problem 5: Autocomplete with a trie
**Algorith Design/Decisions**
* This task was to use a trie to complete an autocomplete function in the provided Jupyter notebook
* The data structures involved in this task were:
  * Trie - Used for efficient storage/lookup of words
  * Hash Map - Used in the trie nodes to store the children nodes for efficient retrieval/insertion
  * Array - Used for storing the potential suffixes

**Time Complexity (Worst Case)**
* The time complexity of this solution is broken down for the individual parts as follows:
  1. Insertion of a new word into the trie - O(n) where n is the number of characters in the word
  2. Search a prefix - O(n) where n is the number of characters in the prefix
  3. Search for a suffx - Simplifies to O(n x m) where n is the length of the children and m is the length of the word
 
**Space Complexity**
* The space complexity for this algorithm is dominated by the number of nodes in the trie O(n)
  * Note that this data structure is efficient for storage since it eliminates repetitive storage of nodes/entities
