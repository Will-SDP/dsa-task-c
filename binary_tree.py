class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        #print(self.value)
        if self.right:
            self.right.traverseInorder()        


class Binary_Tree:

    def __init__(self):
        self.root = None

    def add_recursive(self, current, value):
        if current == None:
            return Node(value)

        if value<current.value:
            current.left = self.add_recursive(current.left, value)
        elif value>current.value:
            current.right = self.add_recursive(current.right,value)
        else:
            return current

        return current

    def add(self, value):
        self.root = self.add_recursive(self.root, value)

    def create_tree(self, data):
        for x in data:
            self.add(x)

    def in_order(self):
        self.root.traverseInorder()            




