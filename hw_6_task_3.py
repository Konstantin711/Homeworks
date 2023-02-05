# 3.
# You have the file text.txt(attached). Please count how many times each letter appears in this file.
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if __name__ == '__main__':

    with open('find_all_letters.txt') as file:
        file_string = file.read()

        for letter in alphabet:
            qty_in_text = re.findall(rf'[{letter + letter.upper()}]', file_string)
            print(f'Letter {letter} in both cases is appeared:', len(qty_in_text))
