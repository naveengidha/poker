from card import Card
from deck import Deck
from evaluator import Evaluator
from lookup import LookupTable

def print_exit_message():
    print("\n\nThank you for playing at the Ace Byn poker room.\n\n")

""" TODO: implement game here
    - set number of players
    - run through streets with evaluations and odds
    - implement betting recommendations
    - repeat until exit
"""

print("\nWelcome to the Ace Byn poker room.")

spots = int(input("\n\nHow many spots would you like at the table? "))

print("\n\nLet's get the cards in the air.")

current_hand = "y"
next_hand = "y"

# main game loop
while next_hand == "y":
    current_hand = "y"
    while current_hand == "y":
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

        current_hand = raw_input("\n\nWould you like to see the flop? ('y'/'n'): ")
        if current_hand == "n":
            break

        print("\n\nBoard: ")
        Card.print_pretty_cards(board)

        # TODO: post flop betting/odds

        # turn
        burn.append(deck.draw(1))
        board.append(deck.draw(1))

        current_hand = raw_input("\n\nWould you like to see the turn? ('y'/'n'): ")
        if current_hand == "n":
            break

        print("\n\nBoard: ")
        Card.print_pretty_cards(board)

        # TODO: post turn betting/odds

        # river
        burn.append(deck.draw(1))
        board.append(deck.draw(1))

        current_hand = raw_input("\n\nWould you like to see the river? ('y'/'n'): ")
        if current_hand == "n":
           break

        print("\n\nBoard: ")
        Card.print_pretty_cards(board)

        # TODO: post river betting/odds

        current_hand = raw_input("\n\nWould you like to see all hands? ('y'/'n'): ")
        if current_hand == "n":
           break

        print("\n\nOpponent's hands: \n")
        for i in range(1, spots):
            print("\n" + str(i) + ": ")
            Card.print_pretty_cards(hands[i])

        print("\n\n")
        evaluator.hand_summary(board, hands)

        # break from inner loop to ask for next hand
        break

    next_hand = raw_input("\n\nWould you like to play the next hand? ('y'/'n'): ")
    if next_hand == "n":
        print_exit_message()
