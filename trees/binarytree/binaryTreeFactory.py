from trees.binarytree.binaryTreeNode import *

def makeBalancedTree(numTiers = 3):
    if numTiers is 0:
        return BinaryTreeNode(None, None, numTiers)

    return BinaryTreeNode( makeBalancedTree(numTiers - 1), makeBalancedTree(numTiers - 1), numTiers )