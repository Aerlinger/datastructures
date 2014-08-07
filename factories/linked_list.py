# Duplicate a Linked List:
def duplicate(head, reverse = false):

  if head != None:
    print("-> " + str(head.getValue()))
    value = head.getValue()
    nextHead = duplicate(head.getNext())

    node = Node(value, nextHead)

    return node

# Traversal:
def traverse(head):
  if head != None:
    print(head)
    traverse(head.getNext())
