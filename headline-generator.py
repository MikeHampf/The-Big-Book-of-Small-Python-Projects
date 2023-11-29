import random

OBJECT_PRONOUNS = ['Her','Him','Them']
POSSESIVE_PRONOUNS = ['Her','His','Their']
PERSONAL_PRONOUNS = ['She','He','They']
STATES = ['California','Texas','Florida','New York','Pennsylvania',
          'Illinois','Ohio','Goergia','North Carolina','Michigan']
NOUNS = ['Athlete','Clown','Shovel','Paleo Diet','Doctor','Parent',
         'Cat','Dog','Chicken','Robot','Video Game','Avacado',
         'Plastic Straw','Serial Killer','Telephone Psychic']
PLACES = ['House','Attic','Bank Deposit Box','School','Basement',
          'Workplace','Donut Shop','Apocalypse Bunker']
WHEN = ['Soon','This Year','Later Today','RIGHT NOW','Next Week']

def main():
    print('Clickbait Headline Generator\nBy A. Sweigart\n')
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to make:')
        response = input('> ')
        if not response.isdecimal():
            print('Enter a number')
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1,2)

        if clickbaitType==1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType==2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType==3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType==4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType==5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType==6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType==7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType==8:
            headline = generateJobAutomatedHeadline()
        print(f'{headline}\n')
    website = random.choice(['wobsite','blag','Facebuuk','Googles',
                             'FacesBook','Tweedie','Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


def generateAreMillennialsKillingHeadline():
    noun=random.choice(NOUNS)
    return f'Are Millenials Killing the {noun} Industry?'

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS)+'s'
    when = random.choice(WHEN)
    return f'Without This {noun}, {pluralNoun} Could Kill You {when}'

def generateBigCompaniesHateHerHeadline():
    pass
def generateYouWontBelieveHeadline():
    pass
def generateDontWantYouToKnowHeadline():
    pass
def generateGiftIdeaHeadline():
    pass
def generateReasonsWhyHeadline():
    pass
def generateJobAutomatedHeadline():
    pass

if __name__=="__main__":
    main()