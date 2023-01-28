# Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
#     a. element is an integer that will be the left operand of the expression
#     b. element is an integer that will be the right operand of the expression
#     c. element is an integer from 1 to 3 where:
#         identifies the addition operation  --- 1
#         identifies the subtraction operation --- 2
#         identifies the multiplication operation --- 3
# d. You can put data into a text file with the text form or use the pickle module in binary form.

# If placed as text then each line should contain only elements of one tuple separated by spaces (eg "100 2 3"). 
# The file must be created by a script in a pre-created \test\data directory tree. 
# The directory tree must be created by the script. Push only the code to the repository (not directories or file).

import random
import os

list_of_tuples = []
path = './test/data/'


def digits_for_tuple():
    left = random.randint(0, 100)
    right = random.randint(0, 100)
    operand = random.randint(1, 3)

    return left, right, operand


if __name__ == '__main__':
    for _ in range(100):
        list_of_tuples.append(digits_for_tuple())

os.makedirs(path)

with open(f'{path}test_data.txt', 'w') as file:
    for line in list_of_tuples:
        file.writelines(f'{line} \n'.replace(',', ' '))
