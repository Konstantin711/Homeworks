# 3
# You have two groups of people. One group consists of omnivores,
# the other only vegetarians. An omnivore is a vegetarian but a
# vegetarian is not an omnivore. Display a list of guests who can eat vegetables and herbs.

omnivore = ['John doe', 'Frank Smith', 'Lucy Frank', 'Silvester Stalone']
vegetarian = ['Jenny Tyler', 'Sad One', 'Frank Sinatra']

all_guests = []

while omnivore:
    guest = omnivore.pop()
    all_guests.append(guest)

    if not omnivore:
        for vegan in vegetarian:
            all_guests.append(vegan)

print(all_guests)
