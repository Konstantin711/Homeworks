# 2.
# Create a function that can return the squares of even elements for the
# range 0 to 1000000000 inclusive. The solution should work and not freeze your computer.


def get_square():
    """It is gen for digits in wide range """
    integer = 0
    while integer <= 1000000000:
        yield integer ** 2
        integer += 2


if __name__ == '__main__':
    result = get_square()

    for i in result:
        print(i)
