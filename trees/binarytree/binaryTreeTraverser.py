class TreeVisitor:

    def __init__(self, node):
        self.node = node
        self.tierNum = 0

    def onVisit(self, callback):
        return callback()

    def traverse(self, node):
        pass

    def visit(self, node):
        self.tierNum += 1
        nodeValue = node.getValue()
        print '\t'*nodeValue + '<' + str(self.tierNum) + '>'
        self.node = node


class InOrderVisitor(TreeVisitor):

    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.getLeft())
        self.visit(node)
        self.traverse(node.getRight())


class PostOrderVisitor(TreeVisitor):

    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.getLeft())
        self.traverse(node.getRight())
        self.visit(node)


class PreOrderVisitor(TreeVisitor):

    def traverse(self, node):
        if node is None:
            return

        self.visit(node)
        self.traverse(node.getLeft())
        self.traverse(node.getRight())


from collections import deque

class BreadthFirstVisitor(TreeVisitor):

    def traverse(self, node):
        queue = deque([node])

        while len(queue) > 0:
            node = queue.popleft()
            self.visit(node)
            if node.getLeft():
                queue.append(node.getLeft())
            if node.getRight():
                queue.append(node.getRight())

