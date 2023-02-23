# 2
# Implement your realization of the function filter
# Note: tasks 2-3 must have the following signature def function_name(callback, sequence).
# Add annotations yourself. Functions must be able to work with integers, floats,
# and strings as elements of sequences.


def custom_filter(function: callable, iterable) -> list:
    """
    This method is custom realization of method filter()
    :param function: Callable object
    :param iterable: Any list of integers, floats, strings
    :return: List
    """

    results = []
    check_func = function(iterable[0])

    if type(check_func) == bool:
        for item in iterable:
            if function(item):
                results.append(item)
            continue
    else:
        print('Method handles only callable that returns bool')

    return results


ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1.4, 15, 1.6, 17, 1.8]
floats = [1.1, 1.3, 1.5, 1.8, 2.0, 3.0, 5.6, 8.6, 4.1, 6.0, 8.0, 10.0, 12.0]
strings = ['one', 'two', 'three', 'four', 'five']


def int_func(x) -> bool:
    if x % 2 == 0:
        return True
    return False


def str_func(x: str) -> bool:
    if len(x) == 3:
        return True
    return False


if __name__ == '__main__':

    # values = custom_filter(int_func, floats)
    values = custom_filter(lambda x: x % 2 == 0, ages)
    print(values)
