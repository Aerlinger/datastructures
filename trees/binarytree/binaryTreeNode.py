class BinaryTreeNode:

    def __init__(self, leftNode, rightNode, value = 'unset'):
        self._value = value
        self.setLeft(leftNode)
        self.setRight(rightNode)

    def getRight(self):
        return self._rightNode

    def getLeft(self):
        return self._leftNode

    def setLeft(self, leftNode):
        self._leftNode = leftNode

    def setRight(self, rightNode):
        self._rightNode = rightNode

    def getValue(self):
        return self._value
