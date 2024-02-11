import random

def generateCards(deck):
    cards = [[], [], []]
    i = 0

    while i < 21:
        count = i%3
        cards[count].append(deck[i])
        i += 1

    return cards

def startRound(rounds, cards):
    if rounds > 2:
        return [card for sublist in cards for card in sublist]

    print('choose one of this cards:\n')
    print('first row', cards[0])
    print('second row', cards[1])
    print('third row', cards[2], '\n')

    row = int(input('which row is your letter on? 1, 2 ou 3?'))
    rowIsInvalid = row not in [1, 2, 3]

    if rowIsInvalid:
        print('restart the program and select a valid row.')
        exit()

    match row:
        case 1:
            cards[0], cards[1] = cards[1], cards[0]
        case 2:
            pass
        case 3:
            cards[1], cards[2] = cards[2], cards[1]

    #transform [[], [], []] in []
    deck = [card for sublist in cards for card in sublist]
    cards = generateCards(deck)

    return startRound(rounds + 1, cards)

print('''
┌──────────────────────────────────────────────────────────────┐
│   ██████╗  ██╗     ██████╗ █████╗ ██████╗ ██████╗ ███████╗   │
│    ╚════██╗███║    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  │
│    █████╔╝╚██║    ██║     ███████║██████╔╝██║  ██║███████╗   │
│    ██╔═══╝  ██║    ██║     ██╔══██║██╔══██╗██║  ██║╚════██║  │
│    ███████╗ ██║    ╚██████╗██║  ██║██║  ██║██████╔╝███████║  │
│    ╚══════╝ ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝  │
│    Created by @NotHiaki on Github                            │
└──────────────────────────────────────────────────────────────┘                 
''')

suits = ['♥', '♠', '♣', '♦']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [value + suit for value in values for suit in suits]

random.shuffle(deck)
cards = generateCards(deck)

rounds = 0
res = startRound(rounds, cards)
print('your card is', res[10])