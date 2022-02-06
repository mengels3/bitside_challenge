import random
from challenge_shop import User, Basket, Inventory

print("+------------------------------------+")
print("| Pre-Work - Initialize requirements |")
print("+------------------------------------+")

# Create User
# User identification using Name and an UUID
# If not defined (e.g. not logged in), the Basket will be assigned to a Guest User with a new UUID
user_name = "Test-User"
user_uuid = "81da050f-9914-498d-ad34-5363bb453e2c"
user = User(user_name, user_uuid)
print("Created User: {}".format(user))
print()

# Create random Invetory 
inventory_size = 10
inventory = Inventory(size=inventory_size)
print("Created a random inventory:")
print(inventory)
print()

# Create empty Basket
basket = Basket(user, inventory)
print("Created a new Basket:")
print(basket)

print()
print("+---------------+")
print("| Pre-Work Done |")
print("+---------------+")
print()
print("+-----------------------------------------------+")
print("| At first: Check basic functionality of basket |")
print("| Add some Items and empty afterwards           |")
print("+-----------------------------------------------+")
print()

# Add a first random item from the Inventory to the basket
print("Add First Item to Basket")
random_number = random.randint(0,inventory_size - 1)
random_item = inventory.items[random_number]
print("Randomly chosen Item from Inventory for scan: Item {}, {}".format(random_number, random_item))
basket.scan(random_item)
print(basket.current_state())
print()

# Add a second random item from the Inventory to the basket
print("Add Second Item to Basket")
random_number = random.randint(0,inventory_size - 1)
random_item = inventory.items[random_number]
print("Randomly chosen Item from Inventory for scan: Item {}, {}".format(random_number, random_item))
basket.scan(random_item)
print(basket.current_state())
print()

print()
print("+-------------+")
print("| Basics done |")
print("+-------------+")
print()

# Empty out basket for discount case
print("Empty out basket for discount cases")
basket.empty_basket()
print(basket.current_state())

print()
print("+-----------------------------------------------+")
print("| Now: activate discounts and again add items   |")
print("| At first: 10% discount on Item 1 of Inventory |")
print("| Then: 2for1 discount on Item 5 of Inventory   |")
print("+-----------------------------------------------+")
print()


# Activate Discount for 2 Articles in Inventory:
# 10 Percent for Article No 1
# "2 for 1" Discount for Article No 5
inventory.items[1].discount = 0.1
inventory.items[5].discount = "2for1"
print("+-------------------------------------------------------------------+")
print("| Added Discounts to Articles 1 (A0001) and 5 (A0005) of inventory: |")
print(inventory)
print("+-------------------------------------------------------------------+")
print()

print("+------------------------------+")
print("| Start with Discount Case 10% |")
print("+------------------------------+")
print()

# Add Item One from the Inventory to the basket
print("Add First Item of Inventory (10%) to Basket")
item_one = inventory.items[1]
print("Chosen Item from Inventory for scan: Item {}, {}".format(1, item_one))
basket.scan(item_one)
print(basket.current_state())

print()
print("+-------------------+")
print("| 10% discount done |")
print("+-------------------+")

print()
# Empty out basket for discount case "2for1"
print("Empty out basket for discount case (2for1)")
basket.empty_basket()
print(basket.current_state())
print()

print("+----------------------------+")
print("| Now: 2 for 1 dicsount case |")
print("+----------------------------+")
print()

# Add Item Five from the Inventory to the basket
print("Add Fifth Item of Inventory (2for1) to Basket")
item_five = inventory.items[5]
print("Chosen Item from Inventory for scan: Item {}, {}".format(5, item_five))
basket.scan(item_five)
print(basket.current_state())
print()

# Add Item Five from the Inventory to the basket for second time --> should be for free
print("Add Fifth Item of Inventory (2for1) to Basket")
item_five = inventory.items[5]
print("Chosen Item from Inventory for scan: Item {}, {}".format(5, item_five))
basket.scan(item_five)
print(basket.current_state())
print()

# Add Item Five from the Inventory to the basket for third time --> should be cost the normale price
# Overall sum has to be twice the value of Item 5. But Item 5 is three times in the basket!
print("Add Fifth Item of Inventory (2for1) to Basket")
item_five = inventory.items[5]
print("Chosen Item from Inventory for scan: Item {}, {}".format(5, item_five))
basket.scan(item_five)
print(basket.current_state())
print()

# Add Item Five from the Inventory to the basket for fourth time --> should be for free again
print("Add Fifth Item of Inventory (2for1) to Basket")
item_five = inventory.items[5]
print("Chosen Item from Inventory for scan: Item {}, {}".format(5, item_five))
basket.scan(item_five)
print(basket.current_state())

print()
print("+---------------------+")
print("| 2for1 discount done |")
print("+---------------------+")

print("+--------------------+")
print("| Testcase finisched |")
print("+--------------------+")
