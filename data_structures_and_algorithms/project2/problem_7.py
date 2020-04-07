#######################################################################
#
#   Problem 7: Request Routing in a Web Server with a Trie (Solution)
#
#######################################################################

class RouteTrie:
    '''Trie to store the routes for efficient lookup'''
    
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)

    def insert(self, route_items, handler):
        '''Insert a route into the route trie'''
        self.root.insert(route_items, handler)

    def find(self, route_items):
        '''Traverse the trie to find the TrieNode if it exists'''
        node = self.root
        for route_item in route_items:
            node = node.children.get(route_item)
            if node is None:
                break
        return node


class RouteTrieNode:
    '''
    Trie node to construct the route trie
        - Only leaf nodes signify valid route ends
    '''
    def __init__(self, handler=None):
        self.handler = handler
        self.children = dict()

    def insert(self, route_items, handler):
        '''Recursive method to insert a new route'''
        if len(route_items) == 0:
            self.handler = handler
            return

        node = self.children.get(route_items[0])
        if node is None:
            node = RouteTrieNode()
            self.children[route_items[0]] = node
        
        node.insert(route_items[1:], handler)
            

class Router:
    '''Router to handle addition and lookup of assigned routes'''

    def __init__(self, root_handler, not_found_handler='404 Not Found'):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, route, handler):
        '''Add a new route/handler combination to the route trie'''
        route_items = self.split_path(route)
        self.route_trie.insert(route_items, handler)

    def lookup(self, route):
        '''
        Search the trie for a route and return it's handler
        or the specified error handler.
        '''
        route_items = self.split_path(route)
        node = self.route_trie.find(route_items)
        if node is None:
            return self.not_found_handler
        elif node.handler is None:
            return self.not_found_handler
        return node.handler

    def split_path(self, route):
        '''Split a path by / and remove any empty items'''
        route_items = []
        for item in route.split('/'):
            if item.strip() != '':
                route_items.append(item)

        return route_items


#######################################################################
#
#   Problem 7: Request Routing in a Web Server with a Trie (Testing)
#
#######################################################################

# Test case setup
router = Router('root handler', 'not found handler')
router.add_handler('/home/about', 'about handler')
router.add_handler('/home/blog/2020/', 'blog 2020 handler')


# Test 1: Root handler
output = router.lookup('/')
print(output)
# Expected result = 'root handler'


# Test 2: Successful route request (non-root)
output = router.lookup('/home/about')
print(output)
# Expected result = 'about handler'


# Test 3: Successful route request (non-root) with a trailing slash
output = router.lookup('/home/about/')
print(output)
# Expected result = 'about handler'


# Test 4: Failed route request (should return error handler)
output = router.lookup('/home/about-me')
print(output)
# Expected result = 'not found handler'




