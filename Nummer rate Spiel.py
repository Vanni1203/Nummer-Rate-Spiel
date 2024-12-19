#Namenseingabe
x = input('Geb deinen Namen ein: ')
print('Hallo, ' + x)

#Programm erzeugt fuer jedes Spiel eine neue Zahl (Zufallsgenerator)
from random import randint
n = randint(1,100)
durchgang = 0
print('Ich habe mir eine Zahl von 1 bis 100 ausgedacht')

#Spieler kann die Zahl versuchen zu erraten
while True:
    durchgang = durchgang + 1
    print('Runde: ' + str(durchgang))
    versuch = int(input('Rate meine Zahl: '))
    
    if versuch == n:
        print('Gut gemacht, du hast meine Zahl erraten ' + x)
        break
    if versuch < n:
        print('die Zahl ist zu klein!')
    else:
        print('die Zahl ist zu gross!')
    if versuch > 100: print('bist du dumm?')

    if (durchgang == 8):
        print('Schade, du hast verloren')
        print('Es war die Zahl ' + str(n))
