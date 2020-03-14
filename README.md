Deuces
========
   
## Installation

```
$ pip install deuces
```

## Usage

Deuces is easy to set up and use. 

```python
>>> from deuces import Card
>>> card = Card.new('Qh')
```

Card objects are represented as integers to keep Deuces performant and lightweight. 

Now let's create the board and an example Texas Hold'em hand:

```python
>>> board = [
>>>     Card.new('Ah'),
>>>     Card.new('Kd'),
>>>     Card.new('Jc')
>>> ]
>>> hand = [
>>>    Card.new('Qs'),
>>>    Card.new('Th')
>>> ]
```

Pretty print card integers to the terminal: 

    >>> Card.print_pretty_cards(board + hand)
      [ A ❤ ] , [ K ♦ ] , [ J ♣ ] , [ Q ♠ ] , [ T ❤ ] 

If you have [`termacolor`](http://pypi.python.org/pypi/termcolor) installed, they will be colored as well. 

Otherwise move straight to evaluating your hand strength:
```python
>>> from deuces import Evaluator
>>> evaluator = Evaluator()
>>> print evaluator.evaluate(board, hand)
1600
```

Hand strength is valued on a scale of 1 to 7462, where 1 is a Royal Flush and 7462 is unsuited 7-5-4-3-2, as there are only 7642 distinctly ranked hands in poker. Once again, refer to my blog post for a more mathematically complete explanation of why this is so. 

If you want to deal out cards randomly from a deck, you can also do that with Deuces:
```python
>>> from deuces import Deck
>>> deck = Deck()
>>> board = deck.draw(5)
>>> player1_hand = deck.draw(2)
>>> player2_hand = deck.draw(2)
```
and print them:

    >>> Card.print_pretty_cards(board)
      [ 4 ♣ ] , [ A ♠ ] , [ 5 ♦ ] , [ K ♣ ] , [ 2 ♠ ]
    >>> Card.print_pretty_cards(player1_hand)
      [ 6 ♣ ] , [ 7 ❤ ] 
    >>> Card.print_pretty_cards(player2_hand)
      [ A ♣ ] , [ 3 ❤ ] 

Let's evaluate both hands strength, and then bin them into classes, one for each hand type (High Card, Pair, etc)
```python
>>> p1_score = evaluator.evaluate(board, player1_hand)
>>> p2_score = evaluator.evaluate(board, player2_hand)
>>> p1_class = evaluator.get_rank_class(p1_score)
>>> p2_class = evaluator.get_rank_class(p2_score)
```
or get a human-friendly string to describe the score,

    >>> print "Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class))
    Player 1 hand rank = 6330 (High Card)

    >>> print "Player 2 hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class))
    Player 2 hand rank = 1609 (Straight)

or, coolest of all, get a blow-by-blow analysis of the stages of the game with relation to hand strength:

    >>> hands = [player1_hand, player2_hand]
    >>> evaluator.hand_summary(board, hands)

    ========== FLOP ==========
    Player 1 hand = High Card, percentage rank among all hands = 0.893192
    Player 2 hand = Pair, percentage rank among all hands = 0.474672
    Player 2 hand is currently winning.

    ========== TURN ==========
    Player 1 hand = High Card, percentage rank among all hands = 0.848298
    Player 2 hand = Pair, percentage rank among all hands = 0.452292
    Player 2 hand is currently winning.

    ========== RIVER ==========
    Player 1 hand = High Card, percentage rank among all hands = 0.848298
    Player 2 hand = Straight, percentage rank among all hands = 0.215626

    ========== HAND OVER ==========
    Player 2 is the winner with a Straight

deuces files from https://github.com/worldveil/deuces