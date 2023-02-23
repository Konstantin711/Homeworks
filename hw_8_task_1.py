# 1
# Implement your own print function. It should work on all operating systems. You can't use build-in print function
import sys


def custom_print(*args):
    """
    This method is printing values to the console
    :param args: Can be used: Str, List, Tuple, Set, Dict,
    :return: None
    """

    if isinstance(args[0], list) or \
            isinstance(args[0], tuple):
        for word in args[0]:
            sys.stdout.write(f'{word} ')

    elif isinstance(args[0], set):
        sys.stderr.write(f'Result for type "Set" can be printed in random order\n')
        for word in args[0]:
            sys.stdout.write(f'{word} ')

    elif isinstance(args[0], dict):
        for word in dict(args[0]).values():
            sys.stdout.write(f'{word} ')

    elif isinstance(args[0], str):
        for word in args:
            sys.stdout.write(f'{word} ')

    else:
        sys.stderr.write(f'Error is appeared. Use data types described in annotation')

    sys.stdout.write(f'\n')


array_to_say = ['Some', 'things', 'that', 'i', 'want', 'to', 'say']
tuple_to_say = ('Some', 'things', 'that', 'i', 'want', 'to', 'say')
set_to_say = {'Some', 'things', 'that', 'i', 'want', 'to', 'say'}
dict_to_say = {1: 'Phrase', 2: 'to say', 3: 55, 4: True}


if __name__ == '__main__':
    custom_print('Some', 'things', 'that', 'i', 'want', 'to', 'say')
    custom_print(dict_to_say)
    custom_print(custom_print)
