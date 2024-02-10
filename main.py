def getSelectedRowAndShuffleCards(row, cards):
    match int(row):
        case '1':
            cards[0], cards[1] = cards[1], cards[0]
        case '2':
            return
        case '3':
            cards[1], cards[2] = cards[2], cards[1]

    tempCards = [card for sublist in cards for card in sublist]
    arr = [[], [], []]

    for i in range(len(tempCards)):
        count = i%3
        arr[count].append(tempCards[i])

    return arr


cards = [
            ['Ac', 'Jp', '9o', '2c', '3s', '4o', '5c'],
            ['6d', '7s', '8s', '9c', 'Ts', 'Jp', 'Qs'],
            ['Ad', '2p', '3d', '4d', '5p', '6d', '7d']
        ]

print('choose one of this cards:\n')
print('first row', cards[0])
print('second row', cards[1])
print('third row', cards[2], '\n')

row = input('which line is your letter on? 1, 2 ou 3?')

if row not in [1, 2, 3]:
    print('restart the program and select a valid row.')

print(getSelectedRowAndShuffleCards(row, cards))