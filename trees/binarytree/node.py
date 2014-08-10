class Node:
    def __init__(self, value='unset', leftNode=None, rightNode=None, parent=None):
        self._value = value
        self.setParent(parent)
        self.setLeft(leftNode)
        self.setRight(rightNode)

    def setParent(self, parent):
        self.parent = parent

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setLeft(self, leftNode):
        self.right = leftNode

    def setRight(self, rightNode):
        self.right = rightNode

    def getValue(self):
        return self.value

    def __repr__(self):
      return "(" + str(id(self.left)) + " <- " + str(id(self)) + ": " + str(self.value) + " -> " + str(id(self.right)) + ")"


class Tree:
    def __init__(self, root = None):
        self.root = root

