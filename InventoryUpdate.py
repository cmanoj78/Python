#! python3
"""
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
The addToInventory() function should return a dictionary that represents
the updated inventory. Note that the addedItems list can contain multiples
of the same item.

"""

treasure = {'gold coin' : 42, 'rope' : 1}

def addToInventory(inv, addedItems):
    print('Original inventory: ')
    print(inv)

    for item in addedItems :
        if item in inv :
            inv[item] += 1
        else :
            inv[item] = 1

    print('items added in this update : ')
    print(addedItems)
    print('Here is the updated inventory: ')
    print(inv)


loot = ['dagger','gold coin', 'potion','rope','gold coin','gold coin']

addToInventory(treasure, loot)
