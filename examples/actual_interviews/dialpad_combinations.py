import unittest

# Problem: Given a 10 digit phone number, produce all combinations of strings that can
# be generated from a dialpad using that phone number

dialpad = [
    ("+"),                  # 0
    (),                     # 1
    ("a", "b", "c"),        # 2
    ("d", "e", "f"),        # 3
    ("g", "h", "i"),        # 4
    ("j", "k", "l"),        # 5
    ("m", "n", "o"),        # 6
    ("p", "q", "r", "s"),   # 7
    ("t", "u", "v"),        # 8
    ("w", "x", "y", "z"),   # 9
]


##
# Input: A number as a string
# Output: A list of number sets representing the dialpad representation of each digit.
#
# Ex.: "23" -> [("a", "b", "c"), ("d", "e", "f")]
def num2set(phone_number):
    result = []
    for digit in phone_number:
        digit = int(digit)
        result.append(dialpad[digit])

    return result

##
# Input: A string and a tuple of characters
# Output: Re-mapped set of possible outputs with given leftmost character
#
# Ex: find_combinations("ab", ("d", "e", "f")) -> ["abd", "abe", "abf"]
def append_combinations(subcode, dialpad_set):
    result = []
    for dialpad_char in dialpad_set:
        result.append(subcode + dialpad_char)

    return result


global_results = set()

##
# Input: a sequence of tuples representing dialpad codes
# Output: All possible pairs of output
#
# Ex: build_subcombinations([("a", "b", "c"), ("d", "e", "f")]) -> ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
def build_subcombinations(input_so_far, input_sequence):
    if len(input_sequence) < 1:
        print input_so_far
        global_results.add(input_so_far)  # TODO: base case return?
        return

    dialpad_chars = input_sequence.pop(0)   # dialpad_chars = ("a", "b", "c"); input_sequence = ("d", "e", "f")

    # append_combinations(input_so_far, dialpad_chars)  # combination_set = ("a", "b", "c")

    for character in dialpad_chars:
        build_subcombinations(input_so_far + character, dialpad_chars)


    # results = []
    # for combination in combination_set:
        # print combination
        # build_subcombinations(combination, input_sequence)
        # nested_combinations = build_subcombinations(combination, input_sequence)
        # print nested_combinations
        # for nested_combination in nested_combinations:
        #     results.append(nested_combination)
            # print result

    # return results

# def iterative_combinations(input_sequence):
#     results = []
#
#     while len(input_sequence) > 0:
#         left_set = input_sequence.pop(0)
#         for char in left_set:
#             results.push[char]




def build_combinations(input):
    pass


assert num2set("2") == [("a", "b", "c")]
assert num2set("23") == [("a", "b", "c"), ("d", "e", "f")]

assert append_combinations("ab", ("d", "e", "f")) == ["abd", "abe", "abf"]
assert append_combinations("a", ("d", "e", "f")) == ["ad", "ae", "af"]
assert append_combinations("", ("d", "e", "f")) == ["d", "e", "f"]


# print build_subcombinations("", [("a", "b", "c"), ("d", "e", "f")])
build_subcombinations("", [("a", "b", "c"), ("d", "e", "f")])
# print global_results
# print build_subcombinations([("d", "e", "f"), ("d", "e", "f")])
# print len(build_subcombinations("a", [("d", "e", "f"), ("d", "e", "f")]))
#assert build_subcombinations("a", [("d", "e", "f")]) == ["ad", "ae", "af"]