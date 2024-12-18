x = input('Geb deinen Namen ein:')
print('Hallo, ' + x)

from random import randint
n = randint(1,100)
print('Ich habe mir eine Zahl von 1 bis 100 ausgedacht')

while True:
    versuch = int(input('Rate meine Zahl: '))
    if versuch == n:
        print('Gut gemacht, du hast meine Zahl erraten ' + x)
        break
    if versuch < n: print('zu klein!')
    if versuch > n: print('zu gross!')