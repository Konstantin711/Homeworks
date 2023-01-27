# Star 2
# you have the same page markup file, but you need to give out a structure in which not the whole
# link but only the domain name: [('google', 'google.com', 'Google'), ('facebook', 'facebook. com', 'Facebook'),
# ('amazon', 'amazon.com', 'Amazon')]

import re


patterns = [r'"(.{6,8})"',
            [r'www.(.{1,50})"\W',
             r'http:..(.{1,50})\/',
             r'href="(.{10})"'],
            r'\W([G,F,A].{3,8})']

parsed_data = []
google = []
facebook = []
amazon = []


def list_to_tuple(array_list):
    return tuple(array_list)


with open('index.html') as file:
    file_ro_read = file.read()

    counter = 1
    for pattern in patterns:

        if counter == 2:
            google.extend(re.findall(patterns[1][0], file_ro_read))
            facebook.extend(re.findall(patterns[1][1], file_ro_read))
            amazon.extend(re.findall(patterns[1][2], file_ro_read))

        else:
            g, f, a = tuple(re.findall(pattern, file_ro_read))
            google.append(g)
            facebook.append(f)
            amazon.append(a)

        counter += 1

for array in [google, facebook, amazon]:
    parsed_data.append(list_to_tuple(array))


print(parsed_data)
