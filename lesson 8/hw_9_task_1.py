# 1
# Create a decorator that prints to the console the name of the function
# that was called. The function should work as intended. For example, create
# a pair of functions for the arithmetic operations of summation and multiplication.
# When calling these functions, the result of the operation must be returned and
# the name of the function that was called must be displayed in the console
# with the result. Small hint (__name__)

def print_called_function(function: callable) -> callable:
    """Decorator to get name of decorated method"""
    def wrapper(a: int, b: int) -> callable:
        """Inner method for decorator"""
        print(function.__name__)
        return function(a, b)
    return wrapper


@print_called_function
def summation(a: int, b: int) -> int:
    """Returns sum of a and b"""
    return a + b


@print_called_function
def multiplication(a: int, b: int) -> int:
    """Returns multiple of a and b"""
    return a * b


if __name__ == '__main__':
    print(summation(55, 34))
    print(multiplication(5, 2))
