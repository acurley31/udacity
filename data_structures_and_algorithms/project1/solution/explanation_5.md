# Data Structures Rationale (Blockchain)
**Data Structures Used:**
* Block (custom class) 
  * Used to store all the associated data for a block in the chain (timestamp, hash, previous block's hash, message, and encoded message)
* Linked List (singly-linked)
  * Used to store the singly-linked block chain
  * This linked list only has a push method since block chains typically do not allow for removal of nodes. There is also no retrieval method.
  
# Space/Time Complexity
**Time Complexity:**
* For inserting a new block into the chain, the time complexity is O(1) as the block is simply appended to the end of the chain
* If a removal or retrieval method were to be added, they would have a worst case time complexity of O(n) since each node would potentially need to be traversed.

**Space Complexity:**
* The space complexity of the block chain implementation is O(n) where n is the number of blocks in the chain
