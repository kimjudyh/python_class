# temp07

inventory = ["revive",
             "potion",
             "potion",
             "pokeball"];
print(inventory);

item = ["banana"];
inventory += item;
print(inventory);

del inventory[1];
print(inventory);

inventory.append("great ball");
print(inventory)

for i in range(0,5,1):
    inventory.append("potion")

print(inventory)

inventory.sort()
print(inventory)

print(inventory.count("potion"))
