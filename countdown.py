import sys,time
import sevseg

while True:
    print("How Long's Your Countdown?")
    response = input('> ')
    if response.isdecimal():
        secondsLeft = int(response)
        break
    else:
        print('Enter numbers only.')
        continue

try:
    while True:
        print('\n'*60)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft%3600)//60)
        seconds=str(secondsLeft%60)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes,2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds,2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow   +'     '+mTopRow    +'     '+sTopRow)
        print(hMiddleRow+'  *  '+mMiddleRow +'  *  '+sMiddleRow)
        print(hBottomRow+'  *  '+mBottomRow +'  *  '+sBottomRow)

        if secondsLeft==0:
            print()
            print('    ****BOOM****')
            break

        print()
        print('Press Ctrl-C tp quit.')

        time.sleep(1)
        secondsLeft-=1

except KeyboardInterrupt:
    print('Countdown, by A. Sweigart')
    sys.exit()