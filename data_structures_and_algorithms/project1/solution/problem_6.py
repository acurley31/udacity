#######################################################################
#
#   Problem 6: Union and Intersection Helper Classes
#
#######################################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


#######################################################################
#
#   Problem 6: Union and Intersection Solution
#
#######################################################################

def intersection(llist_1, llist_2):
    '''Return the intersection of two linked lists as a linked list'''
    used_values = dict()
    union_list = LinkedList()
    node1 = llist_1.head
    while node1:
        value1 = node1.value
        node2 = llist_2.head
        while node2:
            value2 = node2.value
            if (value1 == value2) and (used_values.get(value1) is None):
                union_list.append(value1)
                used_values[value1] = 1
                break

            node2 = node2.next

        node1 = node1.next

    return union_list


def union(llist_1, llist_2):
    '''Return the union of two linked lists as a linked list'''
    intersection_list = LinkedList()
    used_values = dict()
    
    node = llist_1.head
    while node:
        if not used_values.get(node.value):
            intersection_list.append(node.value)
            used_values[node.value] = 1

        node = node.next

    node = llist_2.head
    while node:
        if not used_values.get(node.value):
            intersection_list.append(node.value)
            used_values[node.value] = 1
        node = node.next

    return intersection_list


#######################################################################
#
#   Problem 6: Union and Intersection Test Cases
#
#######################################################################

# Test setup
def build_linked_list(elements):
    linked_list = LinkedList()
    for element in elements:
        linked_list.append(element)
    return linked_list

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21] 
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
element_3 = ['6', 2, '4', 99, None]
llist_1 = build_linked_list(element_1)
llist_2 = build_linked_list(element_2)
llist_3 = build_linked_list(element_3)

# Test 1: Intersection
llist_intersection = intersection(llist_1,llist_2)
print(llist_intersection)
# Expected = [4, 6, 21]


# Test 2: Union
llist_union = union(llist_1, llist_2)
print(llist_union)
# Expected = [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]


# Test 3: Mix of number and string inputs intersection
llist_mixed = intersection(llist_1, llist_3)
print(llist_mixed)
# Expected = [2]















