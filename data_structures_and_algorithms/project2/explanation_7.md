# Problem 7: Request Routing in a Web Server with a Trie
**Algorithm Design/Decisions**
* This task was to develop a web server request router using a trie. As such, the data structures utilized were:
  * Trie - Used for efficient lookup of routes
  * Hash Map - Used for child node storage for the trie nodes due to the efficient retrieval/insertion operations
  * Array - Used in parsing the requested route parts (i.e. everything split by the "/")
  
**Time Complexity (Worst Case)**
* The time complexity for the operations within this task are as follows:
  * Adding a route handler (inserting into the trie) - O(n) where n is the number of parts of the route
  * Looking up a router handler (traversing the trie) - O(n) where n is the number of parts of the route
  * Route part decomposition (splitting by "/") - O(n) where n is the number of characters in the route
  
**Space Complexity**
* The space complexity of this system is dominated by the trie. As such, the approximate space complexity of the request router is O(n) where n is the number of nodes in the trie.
