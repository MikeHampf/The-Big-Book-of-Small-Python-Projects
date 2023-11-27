import random, sys
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by A. Sweigart
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor.  The player must guess if the 
dice total is an even (cho) or odd (han) number.      
      ''')

purse=5000

while True:
    print('You have', purse, 'money.  How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper()=='QUIT':
            print('Thanks for playing, quitter.')
            sys.exit()
        elif not pot.isdecimal():
            print('Enter a number.')
        elif int(pot)>purse:
            print('Your purse is not big enough for that bet.')
        else:
            pot=int(pot)
            break