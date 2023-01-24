# 1
# there is a space-separated string with the names "john peter brian Morgan Adam Maria bart"
# convert the string so that each name starts with a capital letter.

string_to_mod = 'john peter brian Morgan Adam Maria bart'
modified_list = []

for letter in string_to_mod.split(' '):
    modified_list.append(letter.capitalize())


modified_string = ' '.join(modified_list)

print(modified_string)
