import xlrd

from collections import OrderedDict

from cards import Card


class RowMap(object):
    def __init__(self):
        self._row_map = OrderedDict()

    def at(self, idx):
        return self._row_map.get(idx)


class Sheet(object):
    def __init__(self, sheet):
        self.sheet = sheet

        self.row_map = RowMap()

    def _get_data(self, row_num, col_num):
        data = self.sheet.row(row_num)[col_num]

        if data.ctype == xlrd.XL_CELL_NUMBER:
            try:
                return int(data.value)
            except ValueError:
                pass

        return data.value

class CreatureSheet(Sheet):

    def get_creature(self, row_num):
        return Card(
                self.get_id(row_num),
                self.get_name(row_num),
                self.get_cost(row_num),
                self.get_st(row_num),
                self.get_mhp(row_num),
                )

    def get_id(self, row_num):
        return self._get_data(row_num, 0)

    def get_name(self, row_num):
        return self._get_data(row_num, 1)

    def get_rarity(self, row_num):
        return self._get_data(row_num, 2)

    def get_st(self, row_num):
        return self._get_data(row_num, 3)

    #skip hp

    def get_mhp(self, row_num):
        return self._get_data(row_num, 5)

    def get_cost(self, row_num):
        try:
            return self._get_data(row_num, 6)
        except ValueError:
            return self._get_data(row_num, 6)

def get_card_list():
    card_list = []

    # dragon = Card("Dragon", 40, 40, 40)
    # rat = Card("Giant Rat", 0, 40, 40)
    # fighter = Card("Fighter", 20, 30, 40)

    all_data = xlrd.open_workbook("data/culdcept_saga_card_spreadsheet.xls")
    creature_sheet = CreatureSheet(all_data.sheet_by_name("Creatures"))


    card_list += [
        creature_sheet.get_creature(1),
        creature_sheet.get_creature(2),
        creature_sheet.get_creature(3)
    ]



    spell_sheet = all_data.sheet_by_name("Spells")
    item_sheet = all_data.sheet_by_name("Items")


    return card_list
