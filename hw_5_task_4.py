# 4
# you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]

camel_case_words = ["FirstItem", "FriendsList", "MyTuple", "MyTupleTest", "Test1Test2Test3Test4Test5"]
snake_case_array = []

for word in camel_case_words:
    snake_word = ''

    for index, letter in enumerate(word):

        if letter.isupper():
            if index == 0:
                snake_word += letter.lower()
            else:
                snake_word += f'_{letter.lower()}'
        else:
            snake_word += letter.lower()

    snake_case_array.append(snake_word)

print(snake_case_array)

