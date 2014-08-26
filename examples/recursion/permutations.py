# Permute("AB")  =>   ["AB", "BA"]
# Permute("ABC")  =>   ["ABC", "ACB", "BAC", "BCA", "CBA", "CAB"]

input = ['A', 'B', 'C', 'D']

# Favor immutability!!!
def permute(input, k):
    # If we've reached the end of our array, we're done.
    if input and len(input) == k:
        print input

    # For each sequence in this substring:
    for idx in range(k, len(input)):
        swap(input, k, idx)
        permute(input, k + 1)


def swap(input, idx1, idx2):
    temp = input[idx1]
    input[idx1] = input[idx2]
    input[idx2] = temp


permute(input, 0)