from binaryTree.binaryTreeTraverser import *
from binaryTree.binaryTreeFactory import *


balancedTree = makeBalancedTree(3)


print '\nIN-ORDER'
inorder = InOrderVisitor(balancedTree)
inorder.traverse(balancedTree)

print '\nPOST-ORDER'
postorder = PostOrderVisitor(balancedTree)
postorder.traverse(balancedTree)

print '\nPRE-ORDER'
preorder = PreOrderVisitor(balancedTree)
preorder.traverse(balancedTree)

print '\nBREADTH-FIRST'
breadth = BreadthFirstVisitor(balancedTree)
breadth.traverse(balancedTree)