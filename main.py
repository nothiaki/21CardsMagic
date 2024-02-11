import random

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

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
    print('first row ->', Color.GREEN, cards[0], Color.END)
    print('second row ->', Color.GREEN, cards[1], Color.END)
    print('third row ->', Color.GREEN, cards[2], Color.END, '\n')

    row = int(input(Color.GREEN + 'which row is your card on? 1, 2 ou 3?' + Color.END))
    rowIsInvalid = row not in [1, 2, 3]

    if rowIsInvalid:
        print(Color.RED + 'restart the program and select a valid row.' + Color.END)
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

print(Color.GREEN + '''
┌──────────────────────────────────────────────────────────────┐
│   ██████╗  ██╗     ██████╗ █████╗ ██████╗ ██████╗ ███████╗   │
│    ╚════██╗███║    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  │
│    █████╔╝╚██║    ██║     ███████║██████╔╝██║  ██║███████╗   │
│    ██╔═══╝  ██║    ██║     ██╔══██║██╔══██╗██║  ██║╚════██║  │
│    ███████╗ ██║    ╚██████╗██║  ██║██║  ██║██████╔╝███████║  │
│    ╚══════╝ ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝  │
│    Created by @NotHiaki on Github                            │
└──────────────────────────────────────────────────────────────┘                 
''' + Color.END)

suits = ['♥', '♠', '♣', '♦']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [value + suit for value in values for suit in suits]

random.shuffle(deck)
cards = generateCards(deck)

rounds = 0
res = startRound(rounds, cards)
print(Color.GREEN + '''────────────\n     ''' + res[10] + '''\n────────────''' + Color.END)