class Stack:
  __MAX__ = 10

  def __init__(self, items=[]):
    self.items = items

  def push(self, item):
    if len(self.items) > Stack.__MAX__:
      raise "Stack Overflow!"
    return self.items.append(item)

  def pop(self):
    if len(self.items) < 1:
      raise "Stack Underflow!"

    return self.items.pop()

  def __repr__(self):
    print(self.items)
