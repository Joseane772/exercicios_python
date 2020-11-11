from random import randint
t=['jan','ken','po']
pc=t[randint(0,2)]
p = False
while p ==False:
    p = input('jan,ken,po?')
    if p == pc:
        print('tie!')
    elif p == 'jan':
        if pc == 'ken':
            print('you lose!')
        else:
            print('you win')
    elif p == 'ken':
        if pc == 'po':
            print('you lose!')
        else:
            print('you win')
    elif p == 'po':
        if pc == 'jan':
            print('you lose!')
        else:
            print('you win')
p = False
pc = t[randint(0,2)]





