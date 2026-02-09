from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in result:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result[key]
    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
