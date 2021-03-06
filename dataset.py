import xlrd

from collections import OrderedDict

from cards import CreatureCard, EmptyCardRow


class RowMap(object):
    def __init__(self):
        self._row_map = OrderedDict()

    def at(self, idx):
        return self._row_map.get(idx)


class Sheet(object):
    def __init__(self, sheet):
        self.sheet = sheet

        self.row_map = RowMap() #unused

    def _get(self, row_num, col_num):
        data = self.sheet.row(row_num)[col_num]

        if data.ctype == xlrd.XL_CELL_NUMBER:
            try:
                raw_val = float(data.value)
                if raw_val.is_integer():
                    return int(raw_val)
                else:
                    return raw_val
            except ValueError:
                pass

        return data.value

class CreatureSheet(Sheet):
    def get_creature(self, row_num):
        try:
            creature = CreatureCard(
                    self.get_id(row_num),
                    self.get_name(row_num),
                    self.get_cost(row_num),
                    self.get_st(row_num),
                    self.get_mhp(row_num),
                    self.get_description(row_num),
                    )
        except EmptyCardRow as e:
            creature = None

        return creature

    def get_id(self, row_num):
        return self._get(row_num, 0)

    def get_name(self, row_num):
        return self._get(row_num, 1)

    def get_rarity(self, row_num):
        return self._get(row_num, 2)

    def get_st(self, row_num):
        return self._get(row_num, 3)

    #skip hp

    def get_mhp(self, row_num):
        return self._get(row_num, 5)

    def get_cost(self, row_num):
        return self._get(row_num, 6)

    def get_description(self, row_num):
        return self._get(row_num, 11)

def get_card_list():
    card_list = []

    all_data = xlrd.open_workbook("data/culdcept_saga_card_spreadsheet.xls")
    creature_sheet = CreatureSheet(all_data.sheet_by_name("Creatures"))

    try:
        for row_num in xrange(500):
            creature = creature_sheet.get_creature(row_num)
            if creature:
                card_list.append(creature)

    except IndexError: #done monsters
        print "found", row_num


    spell_sheet = all_data.sheet_by_name("Spells")
    item_sheet = all_data.sheet_by_name("Items")


    return card_list
