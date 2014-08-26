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

def process_combinations(input_character_set, combination):
    if len(combination) == len(input_character_set):
        # Sentinel
        print combination
        return

    for character in input_character_set[len(combination)]:
        process_combinations(input_character_set, combination + [character])

process_combinations(num2set("23"), [])
