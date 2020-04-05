#######################################################################
#
#   Problem 1: LRU Cache Helper Classes
#
#######################################################################

class Node(object):
    '''Generic singly-linked node implementation'''

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    '''Generic singly linked list implementation'''

    def __init__(self):
        self.head = None
        self.number_of_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.number_of_elements += 1
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = new_node
        self.number_of_elements += 1
 
    def pop(self, value):
        node = self.head
        if node.value == value:
            self.head = node.next
            self.number_of_elements -= 1
            del node
            return

        while node.next:
            if node.next.value == value:
                tmp = node.next
                node.next = node.next.next
                self.number_of_elements -= 1
                del tmp
                return
 
    def size(self):
        return self.number_of_elements

    def is_empty(self):
        return self.size() == 0
    

class Queue(object):
    '''Simple queue implementation using a singly-linked list'''

    def __init__(self):
        self.head = None
        self.tail = None
        self.number_of_elements = 0

    def enqueue(self, value):
        node = Node(value)
        self.number_of_elements += 1
        if not self.head:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def dequeue(self):
        old_head = self.head
        self.head = self.head.next
        self.number_of_elements -= 1
        value = old_head.value
        del old_head
        return value

    def size(self):
        return self.number_of_elements

    def is_empty(self):
        return self.size() == 0


#######################################################################
#
#   Problem 1: LRU Cache Implementation
#
#######################################################################

class LRU_Cache(object):
    '''LRU cache implementation using a queue and hash map'''

    def __init__(self, capacity):
        self.cache_queue = Queue()
        self.cache_map = dict()
        self.capacity = capacity

    def get(self, key):
        '''Retrieve item from provided key. Return -1 if nonexistent.'''
        value = self.cache_map.get(key)
        if value is not None:
            return value
        return -1
    
    def set(self, key, value):
        '''
        Set the value if the key is not present in the cache. 
        If the cache is at capacity remove the oldest item.
        '''

        if self.cache_queue.size() == self.capacity:
            oldest_key = self.cache_queue.dequeue()
            self.cache_map.pop(oldest_key)

        self.cache_map[key] = value
        self.cache_queue.enqueue(value)


#######################################################################
#
#   Problem 1: LRU Cache Test Cases
#
#######################################################################

# Test 1: (cache hit) Simple get/set of cache values
test1_cache = LRU_Cache(5)
test1_cache.set(1, 1)
test1_cache.set(2, 2)
test1_cache.set(3, 3)

result = test1_cache.get(2)
print(result)
# Expected result = 2


# Test 2: (cache miss) Retrieving a non-existent cache value (value never added to cache)
test2_cache = LRU_Cache(5)
test2_cache.set(1, 1)
test2_cache.set(2, 2)
test2_cache.set(3, 3)

result = test2_cache.get(13)
print(result)
# Expected result = -1


# Test 3: (cache miss) Retrieving an expired cache value (max capacity reached)
test3_cache = LRU_Cache(5)
test3_cache.set(1, 1)
test3_cache.set(2, 2)
test3_cache.set(3, 3)
test3_cache.set(4, 4)
test3_cache.set(5, 5)
test3_cache.set(6, 6)

result = test3_cache.get(1)
print(result)
# Expected result = -1



