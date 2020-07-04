cards = {
    'A': 15,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    's': 2,
    'o': 0
}

def handEquity(hand):
    try:
        equity = 0

        if len(hand) == 2:
            if (hand[0] != hand[1]) or (hand[0] not in cards) or (hand[1] not in cards):
                return -1
            else:
                equity = 2*cards[hand[0]] + cards[hand[1]] + 44

        if len(hand) == 3:
            if (hand[0] not in cards) or (hand[1] not in cards) or (hand[2] not in cards):
                return -1
            if cards[hand[0]] > cards[hand[1]]:
                equity = 2*cards[hand[0]] + cards[hand[1]] + 20 + cards[hand[2]]
            else:
                equity = 2*cards[hand[1]] + cards[hand[0]] + 20 + cards[hand[2]]

        return equity
    except:
        return -1

while(True):
    hand = raw_input("Enter your hand: ")
    print("Your hand equity is: {0}%".format(handEquity(hand)))
    print("------------------------")
