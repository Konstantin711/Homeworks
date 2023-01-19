# 4
# You have a group of guests for the VIP box. The seats in the VIP box
# are all occupied by these guests. There is a group of guests in the
# common room and there are still places in it. Display 2 groups of guests in code.

vip_guests = ['Jenny Tyler', 'Sad One', 'Frank Sinatra']
common_guests = ['John doe', 'Frank Smith', 'Lucy Frank', 'Silvester Stalone', ' ', ' ', ' ', ' ', ' ']

vip_guests.extend(common_guests)

qty = 0

for i in vip_guests:
    if i == ' ':
        qty += 1

print(f'There are {qty} empty seats.')
