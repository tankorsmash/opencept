import enum

DescTypes = enum.Enum("DescTypes", [
    "AttacksFirst",
    "AttacksLast",
    "Defensive",
    "Support",
    "Regenerates",
    "InBattle",
    "Unknown",
])

class DescItem(object):
    desc_type = None

    def __init__(self, raw):
        self.raw = raw

class AttacksFirst(DescItem):
    desc_type = DescTypes.AttacksFirst

class AttacksLast(DescItem):
    desc_type = DescTypes.AttacksLast
    
class Support(DescItem):
    desc_type = DescTypes.Support
    
class Regenerates(DescItem):
    desc_type = DescTypes.Regenerates
    
class InBattle(DescItem):
    desc_type = DescTypes.InBattle
    


class Description(object):
    def __init__(self, raw):
        self.raw = raw
        self.items = raw.split("/")

    def __repr__(self):
        return "<Description: {raw}>".format(
            raw=self.raw[:20],
        )

    def __str__(self):
        return self.raw

