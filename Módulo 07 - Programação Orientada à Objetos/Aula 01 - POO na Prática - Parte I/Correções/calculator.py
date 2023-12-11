from functools import reduce

class Calculator:
    """Calculator representa uma calculadora."""

    def sum(*args):
        return sum(args)
    
    def sub(*args):
        return reduce(lambda acc, curr: acc - curr, args)
    
    def div(*args):
        return reduce(lambda acc, curr: acc / curr, args)
    
    def mul(*args):
        return reduce(lambda acc, curr: acc * curr, args)
