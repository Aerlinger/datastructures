# Taken from: http://beastie.cs.ua.edu/cs150/book/index_17.html

def head(items):
    if not items or items is []:
        return None
    return items[0]


def tail(items):
    if not items or items is []:
        return None
    return items[1:]


def count(items):
    if items is []:
        return 0

    else:
        return 1 + count(tail(items))

# def count_tail(items):
#     if items is not None:
#         return 0
#     else
#         return 1 + count_tail(tail(items))


def accumulate(items):
    if items is None:
        return 0
    else:
        return head(items) + sum(tail(items))

# Filtered count and accumulate:

def countEvens(items):
    if items is None:
        return 0
    elif head(items) % 2 is 0:
        return 1 + countEvens(tail(items))
    else:
        return 0 + countEvens(tail(items))


def occurrences(target, items):
    if items is None:
        return 0
    # If we've found the item
    elif head(items) is target:
        return 1 + occurrences(target, tail(items))
    else:
        return occurrences(target, tail(items))


def isEven(x):
    return x >= 0 and x % 2 == 0

def append(list1, list2):
    list1 + list2


def join(a, b):
    return [a] + [b]

# Filter (select/reduce) Pattern
def extractEvens(items):
    if items is None:
        return None
    # isEven is the select function in this case
    elif isEven(head(items)):
        return join(head(items), extractEvens(tail(items)))
    else:
        return extractEvens(tail(items))


a = [4, 2, 5, 2, 7, 0, 8, 3, 7]
print extractEvens(a)


def map(f, items):
    if items is None:
        return None
    else:
        return join(f(head(items)), map(f, tail(items)))

def find(target, items):
    if items is None:
        return False

    elif(head(items) is target):
        return True

    else:
        return find(target, tail(items))


# Shuffle when both lists are the same length:
def simple_shuffle(list1, list2):
    if list1 is None:
        return None
    else:
        rest = simple_shuffle(tail(list1), tail(list2))
        return join(head(list1), join(head(list2), rest))
