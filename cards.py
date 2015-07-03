
class Card(object):
    def __init__(self, _id, name, cost):
        self.id = _id
        self.name = name
        self.cost = cost

    def __repr__(self):
        return "Card - #{_id} {name} ${c}".format(
            _id = self.id,
            name = self.name,
            c = self.cost,
        )

class CreatureCard(Card):
    def __init__(self, _id, name, cost, st, hp):
        super(CreatureCard, self).__init__(_id, name, cost)

        self.st = st
        self.hp = hp
        self.max_hp = hp

    def __repr__(self):
        return "Creature - #{_id} {name} ${c} {st} {h}/{mh}".format(
            _id = self.id,
            name = self.name,
            c = self.cost,
            st = self.st,
            h = self.hp,
            mh = self.max_hp,
        )
