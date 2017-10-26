#inventory.py
"""
The dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

"""
stuff = {'arrow' : 12, "gold coin" : 42, "rope" : 1, "torch" : 6, "dagger" : 1}

def displayInventory(inventory) :
    total = 0
    print('Inventory : ')
    for item, count in stuff.items():
        print(count, item)
        total = total + count
    print ('Total number of items ',total)


displayInventory(stuff)
