
class Player(object):
    def __init__(self, name, hand):
        self.name = name

        self.hand = hand
        self.hand.player = self
