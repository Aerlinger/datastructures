class Node:
    BLACK = "BLACK"
    RED = "RED"

    def __init__(self, value='unset', leftNode=None, rightNode=None, parent=None, color = None, size = None):
        self.value = value
        self.setParent(parent)
        self.setLeft(leftNode)
        self.setRight(rightNode)
        self.size = size
        self.color = color

    def setBlack(self):
        self.color = Node.BLACK

    def setRed(self):
        self.color = Node.RED

    def getColor(self):
        return self.color

    def setParent(self, parent):
        self.p = parent

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setLeft(self, leftNode):
        self.left = leftNode

    def setRight(self, rightNode):
        self.right = rightNode

    def getValue(self):
        return self.value

    def nil(self):
        return False

    def __repr__(self):
      return "(" + str(id(self.left)) + " <- " + str(id(self)) + ": " + str(self.value) + " -> " + str(id(self.right)) + ")"


class Tree:
    def __init__(self, root = None):
        self.root = root

class NullNode(Node):

    def __init__(self):
        self.color = Node.BLACK

    def nil(self):
        return True
