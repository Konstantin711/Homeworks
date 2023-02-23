# Star 1
# you have html page markup, convert it to structure [('google', 'www.google.com', 'Google'),
# ('facebook', 'http://facebook.com/dign-in', ' Facebook'), ('amazon', 'amazon.com', 'Amazon')]
# using only regular expressions. The first element of the tuple is the id of the container the link is in,
# the second is the link, and the third is the text of the link

import re


patterns = [r'"(.{6,8})"',
            r'f="(.{10,50})"\W',
            r'\W([G,F,A].{3,8})']

parsed_data = []
google = []
facebook = []
amazon = []


def list_to_tuple(array_list):
    return tuple(array_list)


with open('../index.html') as file:
    file_ro_read = file.read()

    for pattern in patterns:
        g, f, a = tuple(re.findall(pattern, file_ro_read))
        google.append(g)
        facebook.append(f)
        amazon.append(a)

for array in [google, facebook, amazon]:
    parsed_data.append(list_to_tuple(array))


print(parsed_data)
