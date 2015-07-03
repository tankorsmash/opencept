
class Card(object):
    def __init__(self, name, cost, st, hp):
        self.name = name
        self.cost = cost
        self.st = st
        self.hp = hp
        self.max_hp = hp

    def __repr__(self):
        return "{name} ${c} {st} {h}/{mh}".format(
            name = self.name,
            c = self.cost,
            st = self.st,
            h = self.hp,
            mh = self.max_hp,
        )
