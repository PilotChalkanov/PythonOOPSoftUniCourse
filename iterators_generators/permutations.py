
from itertools import permutations
def possible_permutations(input_list):
    # Get all permutations of [1, 2, 3]
    perm = permutations(input_list)

    # Print the obtained permutations
    for i in list(perm):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]