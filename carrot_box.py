import random
print('''Carrot in a Box, by A. Sweigart
      This is a bluffing game for two human players.  Each player has a box.
      One box has a carrot in it.  To win, you must have the box with the 
      carrot in it.
      
      This is a very simple and silly game.
      
      The first player looks into their box (the second player must close
      their eyes during this).  The first player then says "There is a carrot 
      in my box" or "There is not a carrot in my box".  The second player then
      gets to decide if they want to swap boxes or not.
      ''')
input('Please Enter to begin...')

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11)+'   '+p2Name[:11].center(11)
print('''HERE ARE TWO BOXES:
   _________      _________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
''')

print()
print(playerNames)
print()
print(p1Name+', you have a RED box in front of you.')
print(p2Name+', you have a GOLD box in front of you.')
print()
print(p1Name+', you will get to look into your box.')
print(p2Name.upper()+', close your eyes and don\'t look!!!')
input('When '+p2Name+' has closed their eyes press Enter...')
print()

print(p1Name+' here is the inside of your box:')

if random.randint(1,2)==1:
    carrotInFirstBox=True
else:
    carrotInFirstBox=False

if carrotInFirstBox:
    print('''
   ____W____ 
  |    W    |
  |    W    |
  |___| |___|     _________
 /    | |  /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (CARROT!)''')
    print(playerNames)
else:
    print('''
   _________ 
  |         |
  |         |
  |_________|     _________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(no carrot!)''')
    print(playerNames)

input('Press enter to continue...')

print('\n' * 100)
print(p1Name+', tell '+p2Name+' to open his/her eyes.')
input('Press Enter to continue...')
print()
print(p1Name+', say one of the following sentences to '+p2Name+'.')
print(' 1) There is a carrot in my box.')
print(' 2) There is not a carrot in my box.')
print()
input('Then press Enter to continue...')
print()

print(p2Name+', do you want to swap boxes with '+p1Name+'? YES/NO')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name+', please enter "YES or NO".')
    else:
        break

firstBox = 'RED '
secondBox = 'GOLD'

if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox
    firstBox, secondBox = secondBox, firstBox

print('''HERE ARE THE TWO BOXES:
   _________      _________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
      '''.format(firstBox, secondBox))
print(playerNames)
input('Press Enter to reveal the winner...')
print()

if carrotInFirstBox:
    print('''
   ____W____      _________
  |    W    |    |         |
  |    W    |    |         |
  |___| |___|    |_________|
 /    | |  /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
    
else:
    print('''
   _________      ____W____
  |         |    |    W    |
  |         |    |    W    |
  |_________|    |___| |___|
 /         /|   /    | |  /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)
if carrotInFirstBox:
    print(p1Name+' is the winner!')
else:
    print(p2Name+' is the winner!')
print("THANKS FOR PLAYING")