from typing import List
from itertools import chain

def matrix_reshape(mat: List[List[int]], rows: int, cols: int) -> List[List[int]]:

    flat=list(chain(*mat))
    if len(flat) != rows*cols:
        return mat

    res = [[] for _ in range(rows)]
    ce = int(len(flat)/rows)
    index = 0

    for element in flat:
        if not len(res[index]) < ce:
            index += 1
        res[index].append(element)
    return res


assert [[1,2,3,4]] == matrix_reshape([[1,2],[3,4]], 1, 4)
assert [[1,2], [3,4]] == matrix_reshape([[1,2],[3,4]], 2, 4)
assert [[1], [2], [3], [4]] == matrix_reshape([[1,2],[3,4]], 4, 1)
assert [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]] == matrix_reshape([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]], 42, 5)
