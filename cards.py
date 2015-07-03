
class Card(object):
    def __init__(self, _id, name, cost, st, hp):
        self.id = _id
        self.name = name
        self.cost = cost
        self.st = st
        self.hp = hp
        self.max_hp = hp

    def __repr__(self):
        return "#{_id} {name} ${c} {st} {h}/{mh}".format(
            _id = self.id,
            name = self.name,
            c = self.cost,
            st = self.st,
            h = self.hp,
            mh = self.max_hp,
        )
