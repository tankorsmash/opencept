import xlrd

from cards import Card

def get_card_list():
    card_list = []

    dragon = Card("Dragon", 40, 40, 40)
    rat = Card("Giant Rat", 0, 40, 40)
    fighter = Card("Fighter", 20, 30, 40)

    
    card_list += [
        dragon,
        rat,
        fighter
    ]

    return card_list
