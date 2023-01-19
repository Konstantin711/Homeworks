# 1
# You have 2 companies with people. One of the companies, let it be Eleks,
# was taken over by Toshiba. Show it in code. Keep in mind that people
# with the same name can be in both companies

eleks = ['Johny D', 'Rich Wood', 'Carla Aster', 'Oliver Good']
toshiba = ['Marry Moore', 'Tim Cook', 'Oliver Good']
toshiba.extend(eleks)
take_over = toshiba

print(take_over)
