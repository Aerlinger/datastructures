# Expanding Exp
# This is very, very difficult.

grammar = [
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]


def expand(tokens, grammar):
    for pos in range(len(tokens)):
        for rule in grammar:
            # hmmmm
            if tokens[pos] == rule[0]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]



depth = 2
utterances = [["exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]


print "# OF UTTERANCES: " + str(len(utterances))

for sentence in utterances:
    print "".join(sentence).replace('-', ' - ').replace('+', ' + ')

#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']