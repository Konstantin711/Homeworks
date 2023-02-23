# 2.
# Write a function square that takes 1 argument, the side of the square,
# and returns 3 values (using a tuple): the perimeter of the square,
# the area of the square, and the diagonal of the square.
import math


def square(side: int) -> tuple:
    """
    Method to calculate square`s features
    :param side: Side of the square
    :return: Tuple: perimeter, area, diagonal
    """

    perimeter = (side + side) * 2
    area = side ** 2
    diagonal = math.sqrt(2) * side

    return perimeter, area, diagonal


if __name__ == '__main__':

    perimeter, area, diagonal = square(10)
    print(perimeter, area, diagonal)
