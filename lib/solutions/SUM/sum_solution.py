# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    raise NotImplementedError()

def sum(num1, num2):
    if not isinstance(num1, int):
        return False
    if not isinstance(num2, int):
        return False
    total = num1 + num2
    return total

