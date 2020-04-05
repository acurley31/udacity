import hashlib
from datetime import datetime

#######################################################################
#
#   Problem 5: Blockchain Solution + Helper Class
#
#######################################################################

class Node(object):
    '''Singly-linked node of a linked list'''

    def __init__(self, data):
        self.data = data
        self.previous = None


class Block(object):
    '''Implementation of a singular block in a blockchain'''
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = str(data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash
    
    def get_previous_hash(self):
        return self.previous_hash

    def get_timestamp(self):
        return self.timestamp

    def get_data(self):
        return self.data


class Blockchain(object):
    '''Singly-linked implementation of a block chain'''

    def __init__(self):
        self.tail = None
        self.number_of_elements = 0

    def __iter__(self):
        '''Iterator to loop over the block's chains in reverse'''
        node = self.tail
        if node is None:
            return
        
        while node:
            yield node
            node = node.previous

    def push(self, data):
        '''Insert a new block at the end of the chain'''
        if data is None:
            return

        timestamp = str(datetime.utcnow())
        previous = self.tail
        block = Block(timestamp, data, previous)
        node = Node(block)
        self.number_of_elements += 1

        if self.tail is None:
            self.tail = node
            return
            
        node.previous = self.tail
        self.tail = node

    def size(self):
        '''Return the number of blocks in the chain'''
        return self.number_of_elements

    def is_empty(self):
        '''Return True if the blockchain is empty otherwise False'''
        return self.size() == 0


#######################################################################
#
#   Problem 5: Test Cases
#
#######################################################################

# Test 1: Inserting blocks
test1_chain = Blockchain()
test1_chain.push('This is the first message')
test1_chain.push('This is the second message')
result = test1_chain.tail.data.data
print(result)
# Expected = 'This is the second message'


# Test 2: Non-string data
test2_chain = Blockchain()
test2_chain.push(13412341)
test2_chain.push(913412)
result = test2_chain.tail.data.data
print(result)
# Expected = '913412' -> numeric value is cast to a string pre-hashing


# Test 3: Invalid input (data = None)
test3_chain = Blockchain()
test3_chain.push('valid first message')
test3_chain.push(None)
test3_chain.push('valid third message')
result = test3_chain.size()
print(result)
# Expected = 2



