from functools import reduce
import operator
from typing import List

def sort_by_bits(arr: List[int]) -> List[int]:
    a = [bin(x)[2:] for x in arr if len(bin(x))]
    groups = {}
    for e in a:
        c = e.count('1')
        if c not in groups.keys():
            groups[c] = []
        groups[c].append(int(e,2))
    groups = sorted(groups.items())
    return reduce(operator.iconcat, [g[1] for g in groups], [])

print(sort_by_bits([10,100,1000,10000]))