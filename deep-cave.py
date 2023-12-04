import random, time, sys

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave, by A. Sweigart')
print('Press Crtl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 20

while True:
    rightWidth = WIDTH-gapWidth-leftWidth
    print(('#'*leftWidth)+(' '*gapWidth)+('#'*rightWidth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    diceRoll=random.randint(1,6)
    if diceRoll == 1 and leftWidth>1:
        leftWidth = leftWidth -1 
    elif diceRoll ==2 and leftWidth+gapWidth<WIDTH-1:
        leftWidth=leftWidth+1
    else:
        pass