# 5
# Implement your own all function


def own_all_method(sequence: list) -> bool:
    """
    Analog of all() method. Returns true if all items returns True, False otherwise
    :param sequence: Any list
    :return: bool
    """
    counter = 0

    for value in sequence:
        if bool(value):
            continue
        else:
            counter += 1
    return True if counter == 0 else False


if __name__ == '__main__':
    print(own_all_method([True, False]))
    print(own_all_method([1, 0]))
    print(own_all_method(['1', '0']))
    print(own_all_method([print, print]))
    print(own_all_method([1.5, 2.0]))
