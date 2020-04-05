#######################################################################
#
#   Problem 3: Huffman Encoding/Decoding Helper Classes
#
#######################################################################

class PriorityQueueNode(object):
    '''Node implementation for a priority queue'''

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None


class PriorityQueue(object):
    '''Generic priority queue implementation'''

    def __init__(self, ascending=False):
        self.head = None
        self.ascending = ascending
        self.number_of_elements = 0

    def enqueue(self, value, priority):
        '''Insert a node based on the specified priority'''
    
        # If an emprty list, set the head node
        new_node = PriorityQueueNode(value, priority)
        self.number_of_elements += 1
        if not self.head:
            self.head = new_node
            return
    
        # If the priority is greater than the head, reset the head node
        if (not self.ascending and priority > self.head.priority) \
            or (self.ascending and priority < self.head.priority):
            new_node.next = self.head
            self.head = new_node
            return

        # Otherwise, traverse the linked list to set the node placement
        node = self.head
        while node.next:
            if (not self.ascending and priority > node.next.priority) \
                or (self.ascending and priority < node.next.priority):
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
    
        node.next = new_node 
        return

    def dequeue(self):
        '''Remove the highest priority element from the queue.
            Returns a tuple of (priority, value).'''
        if self.head is None:
            return 0, None
    
        old_head = self.head
        self.head = old_head.next
        self.number_of_elements -= 1
        return (old_head.priority, old_head.value)


    def size(self):
        '''Return the number of elements in the queue'''
        return self.number_of_elements

    def is_empty(self):
        '''Return if the queue is empty'''
        return self.size() == 0


class TreeNode(object):
    '''Generic tree node implementation'''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        n_children = sum([self.has_left_child(), self.has_right_child()])
        return 'TreeNode ({})'.format(n_children)

    def set_value(self, value):
        self.value = value

    def set_left_child(self, child):
        self.left = child

    def set_right_child(self, child):
        self.right = child

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def is_leaf(self):
        return not self.has_left_child() and not self.has_right_child()


class ReadOnlyTree(object):
    '''Read only tree implementation'''

    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def is_empty(self):
        return self.root is None


#######################################################################
#
#   Problem 3: Huffman Encoding Solution
#
#######################################################################

def huffman_encoding(data):
    '''Encode a string using Huffman compression'''

    # Check for a string input
    if not isinstance(data, str):
        return None, ReadOnlyTree()

    # Compute the frequencies for each of the characters
    frequencies = dict()
    n = len(data)
    for c in data:
        if not frequencies.get(c):
            frequencies[c] = 1
        else:
            frequencies[c] += 1
    
    # Assemble a priority queue for each leaf
    priority_queue = PriorityQueue(ascending=True)
    for c in frequencies:
        priority = frequencies[c]
        priority_queue.enqueue(c, priority)

    while priority_queue.size() != 1:
        left_priority, left_value = priority_queue.dequeue()
        right_priority, right_value = priority_queue.dequeue()
        combined_priority = right_priority + left_priority

        if isinstance(right_value, TreeNode):
            right_node = right_value
        else:
            right_node = TreeNode(right_value)
        
        if isinstance(left_value, TreeNode):
            left_node = left_value
        else:
            left_node = TreeNode(left_value)
        
        node = TreeNode(combined_priority)
        node.set_right_child(right_node)
        node.set_left_child(left_node)

        if priority_queue.is_empty():
            root = node
            break

        priority_queue.enqueue(node, combined_priority)

    # Assign the codenames representing the binary values
    codec = assign_codenames(root, '')
    encoded_data = ''
    for c in data:
        encoded_data += codec[c]

    return encoded_data, ReadOnlyTree(root)


def assign_codenames(node, path, codec=dict()):
    '''Function to recursively traverse the tree and assign the node codenames'''

    if node:
        if node.is_leaf():
            codec[node.value] = path
            node.set_value((node.value, path))
            return codec

        codec = assign_codenames(node.get_left_child(), path + '0')
        codec = assign_codenames(node.get_right_child(), path + '1')

    return codec


#######################################################################
#
#   Problem 3: Huffman Decoding Solution
#
#######################################################################

def huffman_decoding(data, tree):
    '''Decode a binary compression givens its Huffman tree'''

    # Check for a valid input
    if not isinstance(data, str):
        return None
    elif not isinstance(tree, ReadOnlyTree) or tree.is_empty():
        return None

    # Follow the path instructions to decode the data
    path = data
    root = tree.get_root()
    decoded_data = ''
    while len(path) > 0:
        char, path = find_next_character(root, path)
        decoded_data += char

    return decoded_data


def find_next_character(node, path):
    '''Return the next leaf value and the truncated path'''
   
    while node:
        if node.is_leaf():
            return node.value[0], path
        
        if path[0] == '0':
            path = path[1:]
            node = node.get_left_child()
        elif path[0] == '1':
            path = path[1:]
            node = node.get_right_child()


#######################################################################
#
#   Problem 3: Huffman Decoding Test Cases
#
#######################################################################

# Test 1: Encode/decode a simple string
test1_message = 'this is a simple string'
test1_encoded_data, test1_tree = huffman_encoding(test1_message)
test1_decoded_data = huffman_decoding(test1_encoded_data, test1_tree)
print(test1_encoded_data)
print(test1_decoded_data)
print()
# Expected result = 'this is a simple string'


# Test 2: Encode a message with non-alphanumeric characters
test2_message = 'this$ has% &*) some other characters(!#@}{\~~'
test2_encoded_data, test2_tree = huffman_encoding(test2_message)
test2_decoded_data = huffman_decoding(test2_encoded_data, test2_tree)
print(test2_encoded_data)
print(test2_decoded_data)
print()
# Expected result = 'this$ has% &*) some other characters(!#@}{\~~'

# Test 3: Non-string input (invalid)
test3_message = 124197123
test3_encoded_data, test3_tree = huffman_encoding(test3_message)
test3_decoded_data = huffman_decoding(test3_encoded_data, test3_tree)
print(test3_decoded_data)
print(test3_encoded_data)
print()
# Expected result = None



