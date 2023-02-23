# 3
# Implement your own implementation of the function map
# Note: tasks 2-3 must have the following signature def function_name(callback, sequence).
# Add annotations yourself. Functions must be able to work with integers, floats,
# and strings as elements of sequences.


def custom_map(function: callable, *iterable) -> list:
    """
    Function is an analog function map. Can handle one or two arrays
    :param function: Callable object
    :param iterable: Any list of integers, floats, strings
    :return: List
    """
    results = []

    if len(iterable) > 1:
        for first_vale, second_value in zip(*iterable):
            results.append(function(first_vale, second_value))
    else:
        for item in iterable:
            for value in item:
                results.append(function(value))

    return results


ages = [7, 8, 9, 10, 11, 12, 13, 1.4, 15, 1.6, 17, 1.8]
floats = [1.1, 1.3, 1.5, 1.8, 2.0, 3.0, 5.6, 8.6, 4.1, 6.0, 8.0, 10.0]
strings = ['one', 'two', 'three', 'four', 'five']
strings_2 = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']


if __name__ == '__main__':
    array = custom_map(lambda x, y: x+y, strings, strings_2)
    print(array)

    array = custom_map(lambda x: x*2, strings)
    print(array)
