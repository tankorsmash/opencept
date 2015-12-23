
class DescItem(object):
    def __init__(self, raw):
        self.raw = raw


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

