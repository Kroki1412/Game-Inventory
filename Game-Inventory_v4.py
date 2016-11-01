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


def Print_inventory(item, amount):
    reset_global_variables()
    global a
    print('Inventory:')
    while (a != len(item)):
        print(amount[a], item[a], end="\n")
        a += 1


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

#-----The sorting works thanks to the internet... there is space for improvment here


def print_table(order):
    global inv
    keylist_ = list(inv.items())
    b = 0
    c = 0
    print("Inventory:")
    print(" " * 2 + "count" + " " * 4 + "item name")
    print("-" * 20)
    if order == None:
        for key, value in inv.items():
            front_space = 7 - len(str(value))
            mid_space = 20 - front_space - len(str(value)) - len(key)
            print(" " * front_space + str(value) + " " * mid_space + str(key))
            b += value

    elif order == "count,desc":
        while c in range(len(keylist_) - 1):
            if keylist_[c][1] < keylist_[c + 1][1]:
                temp = keylist_[c]
                keylist_[c] = keylist_[c + 1]
                keylist_[c + 1] = temp
                if c > 0:
                    c -= 1
                else:
                    c = 0
            else:
                c += 1
                continue
        for i in range(len(keylist_)):
            front_space = 7 - len(str(keylist_[i][1]))
            mid_space = 20 - front_space - len(str(keylist_[i][1])) - len(keylist_[i][0])
            print(" " * front_space + str(keylist_[i][1]) + " " * mid_space + str(keylist_[i][0]))
            b += keylist_[i][1]

    elif order == "count,asc":
        while c in range(len(keylist_) - 1):
            if keylist_[c][1] > keylist_[c + 1][1]:
                temp = keylist_[c]
                keylist_[c] = keylist_[c + 1]
                keylist_[c + 1] = temp
                if c > 0:
                    c -= 1
                else:
                    c = 0
            else:
                c += 1
                continue

        for i in range(len(keylist_)):
            front_space = 7 - len(str(keylist_[i][1]))
            mid_space = 20 - front_space - len(str(keylist_[i][1])) - len(keylist_[i][0])
            print(" " * front_space + str(keylist_[i][1]) + " " * mid_space + str(keylist_[i][0]))
            b += keylist_[i][1]
    print("-" * 20)
    print("Total number of items:", b)


def import_inventory(filename="import_inventory.csv"):
    global inv
    try:
        file = open(filename, "r")
        keylist_ = file.read().splitlines()
        file.close()
    except:
        print("Error! File ('" + str(filename) + "') does not exist!")
        quit()

    Valuelist_ = []

    for i in range(1, len(keylist_)):
        Valuelist_.append(keylist_[i].split(","))

    del keylist_

    for i in range(len(Valuelist_)):
        Valuelist_[i][1] = int(Valuelist_[i][1])

    for i in range(len(Valuelist_)):
        if Valuelist_[i][0] not in inv:
            inv[Valuelist_[i][0]] = Valuelist_[i][1]
        else:
            inv[Valuelist_[i][0]] += Valuelist_[i][1]


def export_inventory(filename="export_inventory.csv"):
    global inv
    file = open(filename, "w")
    file.write("item_name,count")
    for key, value in inv.items():
        file.write("\n" + str(key) + "," + str(value))
    file.close()


keylist = Create_key_list(inv)
Valuelist = Create_amount_list(inv)
Print_inventory(keylist, Valuelist)

inv = add_to_inventory(inv, dragon_loot)
print(end="\n" * 2)

keylist = Create_key_list(inv)
Valuelist = Create_amount_list(inv)
Print_inventory(keylist, Valuelist)
print('Total number of items:', sum(Valuelist))

print(end="\n" * 2)

print_table(None)
print(end="\n" * 2)
print_table("count,desc")
print(end="\n" * 2)
print_table("count,asc")

print(end="\n" * 2)

import_inventory()
keylist = Create_key_list(inv)
Valuelist = Create_amount_list(inv)
Print_inventory(keylist, Valuelist)
print('Total number of items:', sum(Valuelist))

export_inventory()
