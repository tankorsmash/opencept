#!/usr/bin/env python


from hand import Hand
from cards import Card
from player import Player
from dataset import get_card_list

def main():

    card_list = get_card_list()
    p1_hand = Hand([c for c in card_list[:8]])

    p1 = Player("Player 1", p1_hand)

    # for card in card_list:
    # for card in p1.hand.cards:
    #     print card

    card = card_list[-2]
    print card.description

if __name__ == "__main__":
    main()
