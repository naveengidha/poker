from card import Card
from deck import Deck
from evaluator import Evaluator
from lookup import LookupTable


print("\nWelcome to the Ace Byn poker room.")

spots = int(input("\nHow many spots would you like at the table? "))

print("\nLet's get the cards in the air.")


def print_exit_message():
    print("\nThank you for playing at the Ace Byn poker room.\n")


def print_cards_remaining(num):
    print("\nCards remaining in the deck: %s" % num)


def print_lines():
      print("\n" + "*" * 50)


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
        cards_remaining = 52

        # player hands
        for i in range(spots):
            hand = deck.draw(2)
            cards_remaining = cards_remaining - 2
            hands.append(hand)

        print_lines()
        print("\nYour hand: ")
        Card.print_pretty_cards(hands[0])

        print_cards_remaining(cards_remaining)

        current_hand = raw_input("\nWould you like to see the flop? ('y'/'n'): ")
        if current_hand == "n":
            break

        # flop
        burn.append(deck.draw(1))
        board = deck.draw(3)
        cards_remaining = cards_remaining - 4

        print("\nBoard: ")
        Card.print_pretty_cards(board)

        print_cards_remaining(cards_remaining)

        current_hand = raw_input("\nWould you like to see the turn? ('y'/'n'): ")
        if current_hand == "n":
            break

        # turn
        burn.append(deck.draw(1))
        board.append(deck.draw(1))
        cards_remaining = cards_remaining - 2

        print("\nBoard: ")
        Card.print_pretty_cards(board)

        print_cards_remaining(cards_remaining)

        current_hand = raw_input("\nWould you like to see the river? ('y'/'n'): ")
        if current_hand == "n":
           break

        # river
        burn.append(deck.draw(1))
        board.append(deck.draw(1))
        cards_remaining = cards_remaining - 2

        print("\nBoard: ")
        Card.print_pretty_cards(board)

        print_cards_remaining(cards_remaining)

        current_hand = raw_input("\nWould you like to see all hands? ('y'/'n'): ")
        if current_hand == "n":
           break

        print("\nOpponent's hands:")
        for i in range(1, spots):
            print("\n" + str(i + 1) + ": ")
            Card.print_pretty_cards(hands[i])

        print
        evaluator.hand_summary(board, hands)

        # break from inner loop to ask for next hand
        break

    next_hand = raw_input("\nWould you like to play the next hand? ('y'/'n'): ")

    print_lines()

    if next_hand == "n":
        print_exit_message()

