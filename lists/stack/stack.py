class Stack:
  def __init__(self, items=[]):
    self.items = items

  def push(self, item):
    return self.items.append(item)

  def pop(self):
    if len(self.items) < 1:
      raise "Fail!"

    return self.items.pop()

  def __repr__(self):
    print(self.items)
