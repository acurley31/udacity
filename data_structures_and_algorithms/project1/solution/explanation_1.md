# Data structures rationale

Data structures used:
    - Hash Map
    - Queue

Rationale:
    - The hash map was used for fast retrieval and insertion of new items in the cache since both operations are O(1).
    - Since LRU cache has a finite length, a queue was used to keep track of the order of items added so that when the capacity is reached, the oldest element can be quickly removed.


# Time/Space Complexity

Time Complexity:
    - set(key, value) = O(1)
        - When setting a key, the LRU cache has to only add a new node to the queue which is O(1), add a new item to the hash map O(1), and potentially dequeue the oldest item if the capacity of the LRU cache has been reached O(1). All three operations are O(1) leading to a simplified time complexity of O(1).
    
    - get(key, value) = O(1)
        - When retrieving a key's value, the LRU cache simply has to retrieve the item from the hash map which is O(1)


Space Complexity


