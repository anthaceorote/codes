'''
    Ref: http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

    Morris Traversal:
    Traversing a Threaded Binary Tree -- Creating links to in-order successors, traverse, restore original links
    Advtgs: No recursion
            No stack/ queue -- O(1) memory
'''


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


def inorder_morris_traversal(root):
    curr = root
    visited = []
    while curr:
        if curr.left is None:
            # print(curr.val, end=" ")
            visited.append(curr.val)
            curr = curr.right
        else:
            # Find inorder predecessor of curr
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right

            # Make curr as right child of its predecessor
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                # Fix changes made; Restore the right child of predecessor
                pre.right = None
                # print(curr.val, end=" ")
                visited.append(curr.val)
                curr = curr.right
    return visited


def preorder_morris_traversal(root):
    curr = root
    visited = []
    while curr:
        # If left child is None, visit curr node and move to right child
        if curr.left is None:
            visited.append(curr.val)
            curr = curr.right
        else:
            # Find inorder predecessor of curr
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right

            # If right child of inorder predecessor already points to curr
            # Restore the link and move to right child of curr
            if pre.right is curr:
                pre.right = None
                curr = curr.right
            else:
                # Establish the predecessor link
                pre.right = curr
                visited.append(curr.val)
                curr = curr.left
    return visited


def main():
    '''
    Constructed binary tree is
                1
              /   \
            2      3
          /  \
        4     5
    '''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    assert inorder_morris_traversal(root) == [4, 2, 5, 1, 3]
    assert preorder_morris_traversal(root) == [1, 2, 4, 5, 3]


if __name__ == '__main__':
    main()
