class Node:
  def __init__(self, value = None, next = None):
    self.next = None
    self.value = value

  def getValue(self):
    return self.value

  def setValue(self, value):
    self.value = value

  def setNext(self, next):
    self.next = next

  def getNext(self):
    return self.next
