

import copy as cloner

def copyStr(str):
  strlen = len(str)

  for i in [strlen-1:0]:


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    str(self.getValue())

  def __repr__(self):
    return self.__str__()

  def setValue(self, value):
    self.value = value

  def getValue(self):
    return self.value

  def setPrev(self, prev):
    self.prev = prev

  def setNext(self, next):
    self.next = next

  def getPrev(self):
    return self.prev

  def getNext(self):
    return self.next


def create_dll(nodes):
  for node in nodes:
    pass

def reverse_traverse(tail):
  if(tail):
    print tail.getValue()
    return reverse_traverse(tail.getPrev())


def traverse(head):
  print head.getValue()

  # Copy!
  head_copy = cloner.deepcopy(head)
  head_copy.setValue(head_copy.getValue() + head_copy.getValue())

  if head.next != None:
    # Visit!

    next_copy = traverse(head.next)

    next_copy.setPrev(head_copy)
    head_copy.setNext(next_copy)

    return head_copy
  else:
    head.next = head_copy

    head_copy.setNext(head_copy)

    return head.next

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

print str(id(a))

# print hasattr(a, 'value')
# print getattr(a, 'value')
# print a.getValue()

a.setNext(b)
b.setPrev(a)

b.setNext(c)
c.setPrev(b)

c.setNext(d)
d.setPrev(c)

d.setNext(e)
e.setPrev(d)

# print a.next == b
head = a
tail = e

e_prime = traverse(a)

# print e_prime.getValue()

reverse_traverse(e_prime)

