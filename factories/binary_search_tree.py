from trees.binarytree.node import BinaryTreeNode
from trees.binarytree.binaryTreeTraverser import InOrderVisitor

def build_bst(array):
  if len(array) < 1:
    return None

  midpoint = len(array) / 2
  value = array[midpoint]

  if len(array) > 1:
    lhs = array[0:midpoint]
    rhs = array[(midpoint+1):len(array)]

    return BinaryTreeNode(build_bst(lhs), build_bst(rhs), value)
  else:
    return BinaryTreeNode(None, None, value)


array = [1, 3, 6, 8, 10, 14, 16, 19]

root = build_bst(array)

iov = InOrderVisitor(root)

iov.traverse(root)
