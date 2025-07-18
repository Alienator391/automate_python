def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] +=1
        else:
            inventory[item] = 1
    return inventory    
        
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print("Total number of items: " + str(item_total))

display_inventory(inv)