# Application bitside - Coding Challenge
# Task: https://gist.github.com/N3mezis/e058340930a385d4d4aac513cd0f1c1a#file-codingchallenge-md
import random
from uuid import uuid4

class Inventory():
    # Inventory Class
    # Contains list of items with certain size, Can be created randomly
    
    def __init__(self, size=10):
        self.size = size
        self.items = list()

        for i in range(0, self.size):
            self.items.append(Item('A' + f'{i:04d}', round(random.uniform(0,30), 2)))

    # Creates a random inventory
    def create_new_random_inventory(self):
        self.items = list()
        for i in range(0, self.size):
            self.items.append(Item('A' + f'{i:04d}', round(random.uniform(0,30), 2)))

    def __str__(self):
        return "Inventory with size {}: {}".format(self.size, self.items)

class User():
    # User Class
    # A User has a name and a unique ID
    def __init__(self, name="Guest", uuid=uuid4()):
        self.name = name
        self.uuid = uuid

    def __str__(self):
        return "{} ({})".format(self.name, self.uuid)

class Item():
    # Item Class for Items in Inventory
    # An Item has a name, a price and a possible discount which could be a percentage or a special type like "2for1"
    # Speical discounts need to be implemented within value calculation of basket
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0

    # Overrides
    def __str__(self):
        if self.discount:
            return "Name: {}, Price: {}€, Discount: {}".format(self.name, self.price, self.discount)
        else:
            return "Name: {}, Price: {}€".format(self.name, self.price)

    def __repr__(self):
        return str(self)

    def __eq__(self, other): 
        if not isinstance(other, Item):
            return NotImplemented

        return self.name == other.name and self.price == other.price

class Basket():
    # Basket Class which can hold Items from the assigned Inventory and is assigned to a specific User
    # A Basket contains a dictionary for items, needs an assigned inventory and user
    # Total Value and total amount of items are calculated based on /added(scanned) items

    def __init__(self, user=User(), inventory=Inventory()):
        self.user = user
        self.inventory = inventory
        self.items = dict()
        self.total_items = 0
        self.total_value = 0

    # To String Override
    def __str__(self):
        return """This Basket is assigned to User \"{}\" and has an underlying inventory of {} items.\n\
The Basket currently holds {} element(s) with a total value of {}€: {}""".format(self.user, self.inventory.size, self.total_items, self.total_value, self.items)

    # Get Current State of Basket as String
    def current_state(self):
        return "Basket State: Assigned to User \"{}\", holds {} element(s) with a total value of {}€: {}".format(self.user, self.total_items, self.total_value, self.items)

    # Add(Scan) Item to basket, recalc total sums
    def scan(self, item):
        if type(item) == Item and any(item==inv for inv in self.inventory.items):
            # scanned item is part of inventory
            if item.name in self.items:
                # item already in basket -> increase amount
                self.items[item.name]['amount'] += 1
            else:
                # item not yet in basket -> add
                self.items[item.name] = dict()
                self.items[item.name]['amount'] = 1
                self.items[item.name]['itemtype'] = item

            # recalc values
            self.total_items = self.recalc_total_items()
            self.total_value = self.recalc_total_value()
            print("Added Item {} to the basket of {}".format(item, self.user))
        
        else:
            # scanned item is either nor part of inventory, not a valid item or another error occured
            if type(item) == Item and not any(item==inv for inv in self.inventory.items):
                print("The scanned Item is not part of the inventory of this shop")
            elif type(item) != Item:
                print("The scanned Item is not a valid Item")
            else:
                print("Some kind of error occured while trying to add the Item to this Basket")

    # recalc total value of basket, consider possible discounts of items
    def recalc_total_value(self):
        total_value = 0
        if self.total_items > 0:
            for itemname in self.items:
                item = self.items[itemname]['itemtype']
                if not item.discount:
                    # item has no discount
                    total_value += item.price
                else:
                    # apply discount
                    total_value += self.apply_discount(itemname)
                    
        return round(total_value, 2)

    # apply discount during total value calculation
    def apply_discount(self, itemname):
        item = self.items[itemname]['itemtype']
        if type(item.discount) == float:
            if item.discount in range(0,1):
                # percentage discount
                print("Discount of {}% considered during total value calculation!".format(item.discount * 100))
                discount_value = (item.price * (1-item.discount))
            else:
                # invalid discount (>100%, <0%)
                print("Invalid Discount of {}%, Normal Price used!".format(item.discount * 100))
                discount_value = item.price
        else:
            # special discounts
            if item.discount == "2for1":
                # 2for1 discount
                reduced, remainder = divmod(self.items[itemname]['amount'], 2)
                discount_value = (reduced + remainder) * item.price
                if reduced > 0:
                    print("Discount \"2for1\" considered during total value calculation!")
        return discount_value

    # Total amount of items in basket
    def recalc_total_items(self):
        total_items = 0
        for itemname in self.items:
            total_items += self.items[itemname]['amount']
        return total_items

    # empty out basket
    def empty_basket(self):
        self.items = dict()
        self.total_value = self.recalc_total_value()
        self.total_items = self.recalc_total_items()
        print("Basket is now empty!")

    # remove item from basket
    def remove_item(self):
        raise NotImplementedError("This Function is not implemented yet since it was not needed for the Task!")

