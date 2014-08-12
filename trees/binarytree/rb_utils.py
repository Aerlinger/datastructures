from node import *
from bst_utils import *

def right_rotate(y):
    x = y.left
    if x:
        x.p = y.p
        x.p.right = y

        x.right = y
        y.p = x

        y.left = x.right

def left_rotate(x):
    y = x.right

    if y:
        x.right = y.left
        y.left.p = x

        y.p = x.p
        y.p.left = x
        y.left = x

        x.p = y

def rb_insert_fixup(tree, z):
    # Ensure our RB tree condition:
    while z.p.color is Node.RED:
        # If our parent is a left child of the grandparent:
        if isLeftChild(z.p):
            # Get our "Uncle"
            y = z.p.p.right

            # If the uncle is RED:
            if y.color is Node.RED:
                # Color both our parent and uncle BLACK:
                z.p.color   = Node.BLACK
                y.color     = Node.BLACK

                # Color the grandparent RED:
                z.p.p.color = Node.RED

                # And move our position to the grandparent
                z = z.p.p

            # Otherwise, if we're the right child of our parent
            elif z is z.p.right:
                # Move up to the parent
                z = z.p
                # And rotate to preserve color:
                left_rotate(tree, z)

            z.p.color = Node.BLACK
            z.p.p.color = Node.RED
            right_rotate(tree, z.p.p)
        else:
            # Same as above with right and left exchanged
            pass

    #T.root.color = Node.BLACK

