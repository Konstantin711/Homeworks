# 4.
# You have a file of unknown length.
# Write a function that will remove all numbers from each line of the file.


def remove_numbers_from_file(file_path: str):
    """
    Method removes all digits from file
    :param file_path: path to open a file
    :return: None
    """
    modified_sentences = []
    with open(file_path, 'r+') as file:
        all_sentences = file.readlines()

        for sentence in all_sentences:
            modified_sentence = ''
            for letter in sentence:
                if letter.isdigit():
                    continue
                else:
                    modified_sentence += letter

            modified_sentences.append(modified_sentence)

        file.seek(0)
        file.truncate(0)

        for sentence in modified_sentences:
            file.write(sentence)


if __name__ == '__main__':
    print(remove_numbers_from_file('test.txt'))
