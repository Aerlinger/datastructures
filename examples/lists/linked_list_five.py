from lists.linkedlist.node import Node

head = Node(1)

previous = head

for i in range(1, 6):
  previous.setNext(Node(i))
  previous = previous.getNext()

# Traversal
def traverse(head):
  if head != None:
    print(head.getValue())
    traverse(head.getNext())

traverse(head)

