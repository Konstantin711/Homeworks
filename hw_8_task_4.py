# 4
# Implement your own implementation of function max and min
# (* additional argument amount of result, if you pass 2,
# function should return 2 max values from the list)

digits = [45, 25, 158, -1, 200, 178, 368, -201, 992]


def min_and_max(numbers: list[int], two_max_value: int = None) -> tuple:
    """
    Function to find min and max value from the sequences
    :param numbers: Sequence of digits
    :param two_max_value: Flag to return two maximal digits
    :return: tuple
    """
    min_value = numbers[0]
    max_value = numbers[0]

    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
        else:
            min_value = value

    if two_max_value == 2:
        numbers.remove(max_value)
        second_max_value = 0

        for value in numbers:
            if value > second_max_value:
                second_max_value = value

        return second_max_value, max_value

    return min_value, max_value


if __name__ == '__main__':
    print(min_and_max(digits, two_max_value=2))
    print(min_and_max(digits))




