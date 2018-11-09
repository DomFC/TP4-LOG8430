class Item:
    def __init__(self, name="undefined", unit_price=0, quantity=0):
        self.name = name
        self.quantity = quantity
        self.value = unit_price * quantity


class Invoice:

    def __init__(self):
        self.items = list()
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.total += item.value

    def remove_item(self, item):
        self.items.remove(item)
        self.total -= item.value

    def get_items(self):
        return self.items

    def get_total(self):
        return self.total
