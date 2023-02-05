# 2
# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name.
# Find those who are on all blacklists.

casino_blacklist = {'Sad One', 'John doe', 'Frank Smith', 'Lucy Frank', 'Silvester Stalone'}
poker_blacklist = {'Jenny Tyler', 'Sad One', 'Frank Sinatra', 'David Beckham', 'Silvester Stalone'}
alcohol_blacklist = {'Trever Frost', 'Sad One', 'Silvester Stalone', 'Johny Depp'}

result = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(result)
