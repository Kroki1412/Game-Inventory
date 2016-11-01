import collections
#-------given data
inv = {'rope': 1,
       'torch': 6,
       'gold coin': 42,
       'dagger': 1,
       'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#-------global variables
a = 0
#note to self key list are the first element in the dictionary in this case the items.
keylist = str()
Valuelist = str()


def reset_global_variables():
    global a
    a = 0
    return


def Print_inventory(item, amount):
    reset_global_variables()
    global a
    print('Inventory:')
    while (a != len(item)):
        print(amount[a], item[a], end="\n")
        a += 1
    return

#------create list of dictionarys


def Create_key_list(inventory):
    keylistdict = inventory.keys()
    keylist = list(keylistdict)
    return keylist


def Create_amount_list(inventory):
    valueslistdict = inventory.values()
    valueslist = list(valueslistdict)
    return valueslist

#-------add loot to inventory
#I found it much more easy to just manipulate lists and than remerge them into a dictionary


def add_to_inventory(inventory, added_items):
    a = 0
    global keylist
    while (a != len(added_items)):
        if added_items[a] in keylist:
            b = keylist.index(added_items[a])
            Valuelist[b] += 1
        else:
            keylist.append(added_items[a])
            Valuelist.append(1)
        a += 1
    return dict(zip(keylist, Valuelist))


keylist = Create_key_list(inv)
Valuelist = Create_amount_list(inv)
Print_inventory(keylist, Valuelist)

inv = add_to_inventory(inv, dragon_loot)
print(end="\n" * 2)

keylist = Create_key_list(inv)
Valuelist = Create_amount_list(inv)
Print_inventory(keylist, Valuelist)
print('Total number of items:', sum(Valuelist))
