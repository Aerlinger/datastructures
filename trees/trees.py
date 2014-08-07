from __future__ import print_function
import sys

def outer_insert(tree, element):
    result = insert(tree, element)
    print ("\n<" + str(result).replace("None", "*") + ">")
    return result


def insert(tree, element):
    sys.stdout.write('.')
    if tree == None:
        return (None, element, None)
    else:
        left_child = tree[0]
        this_element = tree[1]
        right_child = tree[2]
        if element <= this_element:
            new_left_child = insert(left_child, element)
            return (new_left_child, this_element, right_child)
        else:
            new_right_child = insert(right_child, element)
            return (left_child, this_element, new_right_child)



# trees = (None, 5, None)
# trees = outer_insert(trees, 2)
# trees = outer_insert(trees, 7)
# trees = outer_insert(trees, 9)
# trees = outer_insert(trees, 10)
# trees = outer_insert(trees, 11)
# trees = outer_insert(trees, 14)
# trees = outer_insert(trees, 1)

#print trees


class Node:
  def __init__(self, value, left=None, right=None):
    self.visited = False
    self.value  = value
    self.left   = left
    self.right  = right

  #def __repr__(self):
#    return str(self.left) + " " + self.value + " " + str(self.right)

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<trees node representation>'

    str(self.value)
    # queue = []





    # node_str = "[" + str(self.value) + "]"
    #
    # if self.left != None:
    #   node_str = node_str + "\t" + str(self.left)
    #
    # if self.right != None:
    #   node_str = node_str + "\t" + str(self.right)
    #
    # return "\t" + node_str


def visit(node, depth = 0):
  if node is not None:
    print("\t"*depth + "[" + str(node.value) + "]")
    node.visited = True
  else:
    print("X")

# Breadth- first search
def bfs(root):
  # Queue tracks which nodes we've visited so we don't visit the same ones twice
  queue = []
  this_level = []

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



t0 = Node(0)
t1 = Node(1)
t2 = Node(2)
t3 = Node(3)
t4 = Node(4)
t5 = Node(5)
t6 = Node(6)


#     t6
#   t2
#     t5
# t0
#     t4
#   t1
#     t3


t0.left   = t1
t0.right  = t2
t1.left   = t3
t1.right  = t4
t2.left   = t5
t2.right  = t6

#bfs(t0)

# def dfs_inorder(node, depth = 0):
#   if node is None:
#     return depth
#
#   depth1 = dfs_inorder(node.left, depth + 1)
#   depth2 = dfs_inorder(node.right, depth + 1)
#
#   max_depth = max(depth1, depth2)
#
#   visit(node, max_depth)

#dfs_inorder(t0, 0)




def dfs_preorder(node, depth = 0):
  if node is None:
    return depth

  visit(node, depth)
  dfs_preorder(node.left, depth + 1)
  dfs_preorder(node.right, depth + 1)

def dfs_inorder(node, depth = 0):
  if node is None:
    return depth

  dfs_inorder(node.right, depth + 1)
  visit(node, depth)
  dfs_inorder(node.left, depth + 1)



def dfs_postorder(node, depth = 0):
  if node is None:
    return depth

  depth1 = 0
  depth2 = 0

  depth2 = dfs_postorder(node.right, depth + 1)
  depth1 = dfs_postorder(node.left, depth + 1)

  max_depth = max(depth1, depth2)

  visit(node, max_depth - depth)

  return max_depth

dfs_preorder(t0, 0)
print("")
dfs_inorder(t0, 0)
print("")
dfs_postorder(t0, 0)


def insert(node, z):
  y = None
  x = node

  while x is not None:
    y = x
    if value < x.value:
      x = x.left
    else:
      x = x.right

  z.p = y

  if y is None:
    return node
  elif z.value < y.value:
    y.left  = z
  else:
    y.right = z
