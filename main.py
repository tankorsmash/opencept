from player import Player
from hand import Hand
from cards import Card

def main():

    dragon = Card("Dragon", 40, 40, 40)
    rat = Card("Giant Rat", 0, 40, 40)
    fighter = Card("Fighter", 20, 30, 40)

    p1_hand = Hand([dragon, rat, fighter])

    p1 = Player("Player 1", p1_hand)

    for card in p1.hand.cards:
        print card

    print "hello world"

if __name__ == "__main__":
    main()
