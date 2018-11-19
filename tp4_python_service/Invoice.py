class Item:
    def __init__(self, name="undefined", unit_price=0, quantity=0):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def print(self):
        print("name: ", self.name, "\tunit_price: ", self.unit_price, "\tquantity: ", self.quantity)


class Invoice:

    # Expected data format is in request_format.json
    def __init__(self, data):
        data_items = data["invoice"]["items"]
        self.items = list()
        [self.items.append(Item(item["name"], item["unit_price"], item["quantity"])) for item in data_items]
        self.print()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def print(self):
        print("Invoice:")
        [item.print() for item in self.items]