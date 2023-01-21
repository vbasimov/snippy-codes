from functools import total_ordering
from pydantic import BaseModel

@total_ordering
class Tree(BaseModel):
    name: str
    height: float | int

    def __lt__(self, other) -> bool:
        return self.height < other.height

    def __le__(self, other) -> bool:
        return self.height <= other.height

    def __gt__(self, other) -> bool:
        return self.height > other.height

    def __ge__(self, other) -> bool:
        return self.height >= other.height

    def __eq__(self, other) -> bool:
        return self.height == other.height

if __name__ == '__main__':
    xmas_tree = Tree(name="Small Fir", height=2.5)
    wisdom_tree = Tree(name="Oak", height=50)

    assert True is (xmas_tree < wisdom_tree)
    assert True is (xmas_tree <= wisdom_tree)

    assert False is (xmas_tree > wisdom_tree)

    xmas_tree.height = wisdom_tree.height = 10
    assert False is (xmas_tree < wisdom_tree)
    assert True is (xmas_tree <= wisdom_tree)
    assert True is (xmas_tree >= wisdom_tree)
    assert True is (xmas_tree == wisdom_tree)
