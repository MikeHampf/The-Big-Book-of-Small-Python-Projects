import sys,time
import sevseg

secondsLeft=30

try:
    while True:
        print('\n'*60)
        hours = str(secondsLeft // 360)


    print(hTopRow+'    '+mTopRow+'    '+sTopRow)
    print(hMiddleRow+' * '+mMiddleRow+' * '+sMiddleRow)
    print(hBottomRow+' * '+mBottomRow+' * '+sBottomRow)

    if secondsLeft==0:
        print()
        print('    ****BOOM****')
        break

    print()
    print('Press Ctrl-C tp quit.')

except KeyboardInterrupt:
    print('Countdown, by A. Sweigart')
    sys.exit()