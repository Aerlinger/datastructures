from node import Node, Tree


def array_to_bst(input):
    input.sort()   # => [1 2 3 4 10 100 200]

    largest = input.pop()

    # Define the root (anchor) node first from the largest element:
    tree = Node(largest)

    while len(input) > 0:
        insert(tree, input.pop)

    return tree

def find_iter(tree, value):
    while tree is not None:
        if tree.getValue() is value:
            return tree

        if value > tree.getValue():
            tree = tree.getRight()
        else:
            tree = tree.getLeft()

def find_min(tree):
    while tree.getLeft() is not None:
        tree = tree.getLeft()

    return tree


def find_max(tree):
    while tree.getRight() is not None:
        tree = tree.getRight()

    return tree

def find(tree, item):
    if tree.getValue() == item or tree is None:
        return tree

    if item > tree.getValue():
        find(tree.getRight(), item)
    else:
        find(tree.getLeft(), item)

def insert(tree, value):
    if tree is None:
        pass

    if value > tree.getValue():
        if tree.getRight() is None:
            tree.setRight(Node(value))
        else:
            insert(tree.getRight(), value)

    elif value < tree.getValue():
        if tree.getLeft() is None:
            tree.setLeft(Node(value))
        else:
            insert(tree.getLeft(), value)

def find_successor(x):
    if x.right:
        return find_min(x.right)

    y = x.parent
    while y and y.right == x:
        x = y
        y = y.parent

    return y

def find_predecessor(x):
    if x.left:
        return find_max(x.left)

    y = x.parent
    while y and y.left == x:
        x = y
        y = y.parent

    return y


def delete_node(tree, item):
    # Establish a reference to the item we want to delete:
    z = find(tree, item)

    # If we don't have any items to the left, we can set our parent to the right sub-tree
    # Note that this covers the condition where both children are Nil as well:
    if z.left is None:
        # Transplant the deleted node with node.right
        transplant(tree, z, z.right)
    # If we don't have any items to the right, we can set the left sub-tree to reference the parent
    elif z.right is None:
        # Transplant the deleted node with node.left
        transplant(tree, z, z.left)
    # Otherwise, we have children on BOTH the left and right
    else:
        # We'll need to replace the deleted node with the minimum value within the right subtree (y):
        y = find_min(z.right)

        # If the smallest value happens to be the head of the subtree, we set y's left child to z's left
        # (For the BST condition we can safely assume that y doesn't have a left subtree)
        if y.parent is not z:
            # Replace z with node.right
            transplant(tree, y, y.right)
            y.right = z.right
            y.right.parent = y

        transplant(tree, z, y)

        # NOTE: y.left will ALWAYS be empty:
        y.left = z.left
        y.left.parent = y

def bfs(root):
    """
    BFS works as follows:

    create a queue and add the root element to the queue

    # Loop:
        # while the queue isn't empty:
        # pop the head of the queue

        # process it

        # push the popped element's children onto the queue (i.e the end of the queue):
    """

    # Queue tracks which nodes we've visited so we don't visit the same ones twice
    queue = []

    depth = 0

    # seed our queue with the root node
    visit(root, len(queue))
    queue.append(root)
    print("pushing: " + str(root.value))

    while queue != []:
        # We've added all this level's children so start popping:
        node = queue.pop(0)
        print("popping " + str(node.value))

        children = [node.left, node.right]

        for child in children:
            if child is not None and not child.visited:
                visit(child, depth)
                print("pushing: " + str(child.value))
                queue.append(child)

def isRightChild(node):
    return node.parent and node.parent.right is node

def isLeftChild(node):
    return node.parent and node.parent.left is node

def transplant(tree, u, v):
    """
     Replaces the subtree rooted at node u, with the subtree rooted at node v. Node u's parent becomes node v's parent. Node
     u's parent becomes node v's parent, and u's parent ends up having v as its appropriate child.

     Note that u remains unmodified
    """

    # If u was the root, v is now the root
    if u.parent is None:
        tree.root = v

    # set u's parent to point to v as the child node
    elif isLeftChild(u):
        u.parent.left = v
    else:
        u.parent.right = v

    # Set v to point to u's parent
    if v is not None:
        v.parent = u.parent




# Traversal
# ####################################################################################################################

def visit(node):
    print(node.getValue())

def inorder(node):
    if node is None:
        return

    inorder(node.getLeft())
    visit(node)
    inorder(node.getRight())


def postorder(node):
    if node is None:
        return

    postorder(node.getLeft())
    postorder(node.getRight())
    visit(node)


def preorder(node):
    if node is None:
        return

    visit(node)
    preorder(node.getLeft())
    preorder(node.getRight())

def print_tree(node):
    inorder(node)




def array_to_bst(input):
    input.sort()   # => [1 2 3 4 10 100 200]

    largest = input.pop()

    # Define the root (anchor) node first from the largest element:
    tree = Node(largest)

    while len(input) > 0:
        value = input.pop()
        print("Inserting: " + str(value))
        insert(tree, value)

    return tree
