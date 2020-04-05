# Data Structures Rationale (LRU Cache)
**Data structures used:**
* Hash map
  * Used for fast retrieval (get) and insertion (set) of new items in the cache since both operations are O(1)
* Queue
  * Since LRU cache has a finite length, a queue was used to keep track of the order of items added
  * This was done such that when the capacity is exceeded upon insertion, the oldest element can be removed before the new element is added with a time complexity of O(1)



# Time/Space Complexity
**Time Complexity:**
* set(key, value) = O(1)
  * When setting a key, the LRU cache has to perform the following operations:
    1. Add a new node to the queue which is O(1)
    2. Add a new item to the hash map O(1)
    3. And potentially dequeue the oldest item if the capacity of the LRU cache has been reached O(1). 
  * All three operations are O(1) leading to a simplified time complexity of O(1).
    
* get(key, value) = O(1)
  * When retrieving a key's value, the LRU cache simply has to perform the following operations:
    1. Retrieve the item from the hash map which is O(1)
  * This operation is O(1) and therefore, the simplified time complexity is O(1)


**Space Complexity:**
* Since this implementation of LRU cache uses two data structures (queue and hash map) that are both dependent on the pre-determined capacity of the cache, the space complexity is O(n) where n is the capacity


