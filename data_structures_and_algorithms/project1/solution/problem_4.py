#######################################################################
#
#   Problem 4: Active Directory Helper Classes
#
#######################################################################

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


#######################################################################
#
#   Problem 4: Active Directory Solution
#
#######################################################################

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    for group_user in group.get_users():
        if group_user == user:
            return True

    subgroups = group.get_groups()
    for subgroup in subgroups:
        stat = is_user_in_group(user, subgroup)
        if stat:
            return True

    return False

#######################################################################
#
#   Problem 4: Active Directory Test Cases
#
#######################################################################

# Test case setup
user1 = 'user1'
user2 = 'user2'
user3 = 'user3'

group1 = Group('Group 1')
group1_child1 = Group('Group 1 / Child 1')
group1_child1.add_user(user1)
group1_child1.add_user(user2)
group1_child2 = Group('Group 1 / Child 2')
group1_child2.add_user(user3)
group1.add_group(group1_child1)
group1.add_group(group1_child2)

group2 = Group('Group 2')
group2_child1 = Group('Group 2 / Child 1')
group2_child1_child1 = Group('Group 2 / Child 1 / Child 1')
group2.add_group(group2_child1)
group2.add_group(group2_child1_child1)


# Test 1: User has group permission 
test1_group = group1
test1_user = user2
result = is_user_in_group(test1_user, test1_group)
print(result)
# Expected result = True


# Test 2: User does not have permission, but exists in sibling group
test2_group = group1_child1
test2_user = user3
result = is_user_in_group(test2_user, test2_group)
print(result)
# Expected result = False


# Test 3: Group does not have any users
test3_group = group2_child1_child1
test3_user = user2
result = is_user_in_group(test3_user, test3_group)
print(result)
# Expected result = False




