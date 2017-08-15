class BinaryTreeNode:
    ''' Node class for a Binary Tree '''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        return self.data

    @property
    def left(self):
        return self.left

    @property.setter
    def left(self, left):
        self.left = left

    @property
    def right(self):
        return self.right

    @property.setter
    def right(self, right):
        self.right = right

    @classmethod
    def new_node(cls, data, left, right):
        node = cls(data)
        node.left = left
        node.right = right
        return node

    def __repr__(self):
        return 'BinaryTreeNode({}})'.format(self.data)

    def __str__(self):
        return str(self.data)

    def display(self):
        return 'Binary Tree Node {}, Left --> {}, Right --> {}'.format(self.data, self.left, self.right)


class BinaryTree:
    def preorder_recursive(root):
        if root:
            print(root.data, end=' ')
            preorder_recursive(root.left)
            preorder_recursive(root.right)

    def preorder(root):
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()
            print(node.data, end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inorder_recursive(root):
        if root:
            inorder_recursive(root.left)
            print(root.data, end=' ')
            inorder_recursive(root.right)

    def inorder(root):
        if not root:
            return

        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.data, end=' ')
                node = node.right

    def postorder_recursive(root):
        if root:
            postorder_recursive(root.left)
            postorder_recursive(root.right)
            print(root.data, end=' ')

    def postorder(root):
        if not root:
            return

        visited = set()
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    print(node.data, end=' ')
                    node = None

    def get_size(root):
        if not root:
            return 0
        return get_size(root.left) + get_size(root.right) + 1

    def get_height(root):
        if not root:
            return 0
        return max(get_height(root.left), get_height(root.right)) + 1


''' Tree Traversals -- C:Current(Root), L:Left, R:Right
Preorder    CLR     Stack
Inorder     LCR
Postorder   LRC
Level-order BFS     Queue
'''
