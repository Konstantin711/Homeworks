"""Create an iterator that accepts a sequence and can iterate over values in a given range.
CustomIterator(sequence, start_index, end_index)"""


class CustomIterator:
    """Iterator receives start index and end index. Iterator returns values including end index"""
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self._sequence = sequence
        self._start_index = start_index
        self._end_index = end_index

    def __setattr__(self, key, val):
        if key == '_end_index':
            if self.__dict__['_start_index'] > val:
                raise SyntaxError('Start index should be less than End index')
        self.__dict__[key] = val

    def __iter__(self):
        return self

    def __next__(self):
        if self._start_index < len(self._sequence) and self._start_index <= self._end_index:
            val = self._sequence[self._start_index]
            self._start_index += 1
            return val
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iter = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1, 5)

    for value in custom_iter:
        print(value)
