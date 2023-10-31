import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA==birthdayB:
                return birthdayA
print('''Birthday Paradox, by A. Swiegart
      
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated reandom 
    simulations) to explore this concept.''')

MONTHS = ('Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec')

while True:
    print('How many birthdays shall I generate?  (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0<int(response)<=100):
        numBDays = int(response)
        break
print()

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday, in enumerate(birthdays):
    if i!=0:
        print(', ', end='')
        monthName=MONTHS[birthday.month-1]
        dateText='{} {}'.format(monthName, birthday.day)
        print()
        print()

match = getMatch(birthdays)

print('In this simulation, ', end='')
