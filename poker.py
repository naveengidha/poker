from card import Card
from deck import Deck
from evaluator import Evaluator
from lookup import LookupTable

""" TODO: implement game here
    - set number of players
    - run through streets with evaluations and odds
    - implement betting recommendations
    - repeat until exit
"""

print("\nWelcome to the Byn poker room.")

spots = int(input("\n\nHow many spots at the table? "))

print("\n\nLet's get the cards in the air.")

deck = Deck()
hands = []
burn = []

while True:
    # player hands
    for i in range(spots):
        hand = deck.draw(2)
        hands.append(hand)

    print("\n\nYour hand: ")
    Card.print_pretty_cards(hands[0])

    # TODO: pre flop betting

    burn.append(deck.draw(1))
    board = deck.draw(3)

    print("\n\nBoard: ")
    Card.print_pretty_cards(board)

    # TODO: post flop betting

    burn.append(deck.draw(1))
    board.append(deck.draw(1))

    print("\n\nBoard: ")
    Card.print_pretty_cards(board)

    # TODO: post turn betting

    burn.append(deck.draw(1))
    board.append(deck.draw(1))

    print("\n\nBoard: ")
    Card.print_pretty_cards(board)

    # TODO: post river betting

    print("\n\nOpponent's hands: ")
    for i in range(1, spots):
        print("\n" + str(i) + ": ")
        Card.print_pretty_cards(hands[i])

    exit(1)
