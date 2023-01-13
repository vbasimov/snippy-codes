from typing import Callable

def chain_sum(i: int = None) -> Callable:
    state = i

    def func(i2: int = None) -> Callable | int:
        nonlocal state
        if i2 is None:
            return state
        state += i2
        return func

    return func

assert 2 == chain_sum(2)()
assert 18 == chain_sum(10)(8)()
assert 77 == chain_sum(0)(100)(-20)(-3)()

print("Ok")
