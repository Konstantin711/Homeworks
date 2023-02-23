# 5
# You have a group of people with non-unique names. Generate a list of non-duplicate
# names (you cannot use set for this task. If there are 2 johns in the list,
# you need to take only one of them. "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

non_uniq = ['Jenny Tyler', 'Sad One', 'Frank Sinatra', 'Sad One', 'Frank Sinatra', 'Jenny Tyler', 'Sad One', 'Frank Sinatra']

non_duplicates = list(dict.fromkeys(non_uniq))

print(non_duplicates)
