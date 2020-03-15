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

print("\nWelcome to the Ace Byn poker room.")

spots = int(input("\n\nHow many spots would you like at the table? "))

print("\n\nLet's get the cards in the air.")

action = "y"

# main game loop
while action == "y":
    deck = Deck()
    evaluator = Evaluator()
    hands = []
    burn = []

    # player hands
    for i in range(spots):
        hand = deck.draw(2)
        hands.append(hand)

    print("\n\nYour hand: ")
    Card.print_pretty_cards(hands[0])

    # TODO: pre flop betting/odds

    # flop
    burn.append(deck.draw(1))
    board = deck.draw(3)

    action = raw_input("\n\nWould you like to see the flop? ('y'/'n'): ")
    if action == "n":
        exit(1)

    print("\n\nBoard: ")
    Card.print_pretty_cards(board)

    # TODO: post flop betting/odds

    # turn
    burn.append(deck.draw(1))
    board.append(deck.draw(1))

    action = raw_input("\n\nWould you like to see the turn? ('y'/'n'): ")
    if action == "n":
        exit(1)

    print("\n\nBoard: ")
    Card.print_pretty_cards(board)

    # TODO: post turn betting/odds

    # river
    burn.append(deck.draw(1))
    board.append(deck.draw(1))

    action = raw_input("\n\nWould you like to see the river? ('y'/'n'): ")
    if action == "n":
       exit(1)

    print("\n\nBoard: ")
    Card.print_pretty_cards(board)

    # TODO: post river betting/odds

    action = raw_input("\n\nWould you like to see all hands? ('y'/'n'): ")
    if action == "n":
       exit(1)

    print("\n\nOpponent's hands: \n")
    for i in range(1, spots):
        print("\n" + str(i) + ": ")
        Card.print_pretty_cards(hands[i])

    print("\n\n")
    evaluator.hand_summary(board, hands)

    action = raw_input("\n\nWould you like to play the next hand? ('y'/'n'): ")
    if action == "n":
        print("\n\nThank you for playing. See you next time.\n\n")
        action = "n"
