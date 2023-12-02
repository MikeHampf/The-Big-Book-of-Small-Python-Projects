import copy, random, sys, time

WIDTH=79
HEIGHT=20

ALIVE = 'O'
DEAD = ' '

nextCells={}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            nextCells[(x,y)]=ALIVE
        else:
            nextCells[(x,y)]=DEAD

while True:
    print('\n'*50)
    cells=copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)],end='')
        print()
    print('Press Ctrl-C to quit')