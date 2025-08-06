treasure = {"clues": ["beach", "cave", "waterfall"],"locations": {"beach": {
            "items": ["compass", "shovel"],
            "hint": "dig here"},"cave": {
            "items": ["lantern", "gold coin"],
            "hint": "look behind rocks"},"volcano": {
            "items": ["diamond", "lava boots"],
            "hint": "wear protection"}},"crew": ["First Mate", "Cook"]}

treasure["clues"].append("volcano")

print( ", ".join(treasure["crew"]))

print(" Possible locations to explore:")
for clue in treasure["clues"]:
    print( clue)

while True:
    choice = input(" Where do you want to search? (type 'quit' to exit): ")
    if choice == "quit":
        print(" Farewell, Captain! Until next time.")
        break

    if choice in treasure["locations"]:
        location = treasure["locations"][choice]
        print(" Hint:", location["hint"])
        print("You found:", ", ".join(location["items"]))

        if "gold coin" in location["items"]:
            print(" You found the GOLD COIN! You win!")
            break
        else:
            print(" No treasure here. Keep searching")
    else:
        print("That's not a known location. Try again")