# 3
# here is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: euro}

name = " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".strip()
name = name.replace('&&', ' ').replace('&', ' ')

cleaned_array = name.split(' ')
cleaned_array[0] = cleaned_array[0][:11]

cleaned_dict = {}

for pair in cleaned_array:
    key, value = (pair.split('='))
    cleaned_dict.update({key: value})

print(cleaned_dict)
