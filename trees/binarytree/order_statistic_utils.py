from node import *

def os_select(x, i):
    r = x.left.size + 1

    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i - r)

