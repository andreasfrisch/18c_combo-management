# Author: Andreas Frisch
# Date: 13/2 2021
#
# Prints combinations of x distinct elements from set of n elements

from itertools import combinations as calc_combs

ACTIONS = [
    "Activate",
    "Buy",
    "Gain 1",
    "Trade",
    "Swap",
    "Discard 2",
    "Destroy 1",
]

combinations = calc_combs(ACTIONS, 4)
for combination in combinations:
    print(combination)
