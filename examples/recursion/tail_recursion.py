# Without tail recursion:
def recsum(x):
  if x == 1:
    return x
  else:
    return x + recsum(x - 1)

def recsum_tail(x, accumulator = 0):
  if x == 1:
    return accumulator
  else:
    return recsum_tail(x - 1, accumulator + x)



print(recsum_tail(5))

print(5 + (recsum(4)))
print(5 + 4 + recsum(3))
print(recsum(recsum(recsum(recsum(2)))))
print(recsum(recsum(recsum(recsum(recsum(1))))))
