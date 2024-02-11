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
    cardsList = [card for sublist in cards for card in sublist]
    cards = [[], [], []]

    for i in range(len(cardsList)):
        count = i%3
        cards[count].append(cardsList[i])

    return startRound(rounds + 1, cards)

cards = [
    ['A♥', 'J♠', '9♣', '6♣', '3♠', 'Q♣', '5♣'],
    ['6♦', '7♠', '8♠', '9♠', 'Q♠', 'J♦', 'K♠'],
    ['A♦', '2♥', '3♦', 'A♠', '5♥', '4♥', '7♦']
]

print('''
┌──────────────────────────────────────────────────────────────┐
│   ██████╗  ██╗     ██████╗ █████╗ ██████╗ ██████╗ ███████╗   │
│    ╚════██╗███║    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  │
│    █████╔╝╚██║    ██║     ███████║██████╔╝██║  ██║███████╗   │
│    ██╔═══╝  ██║    ██║     ██╔══██║██╔══██╗██║  ██║╚════██║  │
│    ███████╗ ██║    ╚██████╗██║  ██║██║  ██║██████╔╝███████║  │
│    ╚══════╝ ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝  │
│    Created by @NotHiaki in Github                            │
└──────────────────────────────────────────────────────────────┘                 
''')

rounds = 0
x = startRound(rounds, cards)
print('your card is', x[10])