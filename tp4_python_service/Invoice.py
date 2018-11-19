class Item:
    def __init__(self, name="undefined", unit_price=0, quantity=0):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price


class Invoice:

    def __init__(self):
        self.items = list()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items