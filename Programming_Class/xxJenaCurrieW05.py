bag=[]
u = "\033[4m"
b = "\033[1m"
i = "\033[3m"
clr = "\033[0m"
"""to add to list"""
def AddToBag (item):
    bag.append (item)
"""to remove from list"""
def RemoveFromBag (item):
    bag.remove (item)

def CheckInventory():
    print(f"{i}Your bag has: ")
    print(f"{bag}{clr}")
    
    

def NonRoom():
    room = input("Where do you want to go? ")
    if room.upper() == "STAIRS":
        lab()
    elif room.upper() == "TOWER":
        tower()
    elif room.upper() == "SEARCH":
        ruins()
    elif room.upper() == "EXPLORE":
        gardens
    else: CheckInventory()

def NonItem():
    use = input("What item do you want to use? ")
    print(bag)
    if use.upper() == "TORCH":
        torch()
    elif use.upper() == "FABRIC":
        fabric()
    elif use.upper() == "BOTTLE":
        bottle()
    else: print("Can't seem to find a use for that item.")
    CheckInventory()

"""ROOMS"""
def start():
    print("\n")
    print("--------------------------------------------------------------------------------------")
    print("Wha-where am I?")
    print("You push yourself to a sit as you're slowly gaining consciousness.")
    print("The dim twilight barely reveals the ruins of an old castle tower around you.")
    print("As you stand up to dust yourself off, you notice an unfamiliar satchel at your hip.")
    print("You open it as your gaze follows your hand and inside it, you see:")
    print(f"a small corked {u}{i}BOTTLE{clr}, a large peice of {u}{i}FABRIC{clr} and a {u}{i}TORCH{clr}.")
    print("\n")
    use = input(f">> {u}Which item do you pull out?{clr} ")
    if use.upper() == "FABRIC":
        fabric()
    elif use.upper() == "BOTTLE":
        bottle()
    elif use.upper() == "TORCH":
        torch()
    else: NonItem()
    
def lab():
    print("\n")
    print("You s.l.o.w.l.y and carefully start down the stairs.")
    print("Amazingly, you reach the bottom safely!")
    print("\n") 
    print("You set your torch into a sconce in what seems to be an old Apothecary lab.")
    print("The light reveils a shelf nearby and the oddly shaped jars catch your eye.")
    print(f"Scanning the shelf, you see a jars labeled {i}Squid {u}TOES{clr}, {i}Powdered {u}WATER{clr} and {i}Baking {u}SODA{clr}.")
    print("\n")
    print("Not wanting to weigh down your satchel, you only want to take one bottle.")
    take = input(f">>{u}Which do you take?{clr} ")
    if take.upper() == "TOES":
        AddToBag ("SQUID_TOES")
    elif take.upper() == "WATER":
        AddToBag ("POWDERED_WATER")
    elif take.upper() == ("SODA"):
        AddToBag ("BAKING_SODA")
    else: AddToBag ("BAKING SODA")
    CheckInventory()
    print("\n")
    print(f"As you're putting your {i}{take.upper}{clr} in your bag, ")
    print("you notice an opening through which you can barely make out the shadows of grass")
    print("You walk out the door to settle on some more ruins.")
    print("Suddenly, you get the creepy feeling someone is watching you.")
    room = input ("Do you want to SEARCH the ruins for a weapon or EXPLORE the gardens?")
    if room.upper() == "SEARCH":
        ruins()
    elif room.upper() == "EXPLORE":
        gardens()
    else: NonRoom()
    
def tower():
    print("You walk down the narrow, cold stone pathway and enter the other tower.")
    print("By the bright light of the torch, you can see a scorched portrait on the tower wall.")
    print("Princess Etherea Chimericus: Keeper of the Dreams") 
    print("you can barely make out the faint engraving")
    print("on the small gold plaque under the large frame. ")
    print("\n")
    print("'Keeper of Dreams?' you wonder and your focus drops to the ground.")
    print("On the ruin ground, just in front of your foot, your eyes catch the glint")
    take = input("of a gold coin. TAKE the coin or LEAVE it there?")
    if take.upper() == "TAKE":
        AddToBag ("GOLD_COIN")
    else:
        print("\n")
        print("Suddenly, you remember how to breeze caught that fabric in your bag.")
        use = input ("Do you use the fabric to JUMP or go back and use the STAIRS? ")
        print("\n")
        if use.upper == "JUMP":
            jump()
        elif use.upper == "STAIRS":
            lab()
        else: NonRoom()

def ruins():
    print("Leading with the torch to ward off anything dangerous from approaching you, you cautiously look around the ruins.")
    print("Trying to make as little noise as possible, you carefully turn over the large stones that were once fortress walls.")
    print("Out of the corner of your eye, you see the lit torch reflecting back at you.")
    print("A sword!")
    print("Somehow it fits into your new magic satchel and you feel much safer going to explore the gardens.")
    AddToBag("SWORD")
    print("\n")
    print("Behind you, you notice a moat.")
    room = input ("Do you want to walk to the MOAT or EXPLORE the gardens?")
 #   if room.upper() == "MOAT":
#!!        moat()
    if room.upper() == "EXPLORE":
        gardens()
    else: NonRoom()

def gardens():
    print("Leading with the torch to ward off anything dangerous from approaching you, you start off toward the gardens.")

"""ITEMS"""
def fabric():
    print("\n")
    print("You unfold the large piece of fabric. As you’re examining it, the wind catches it and nearly blows it out of your hand.")
    print("Quickly catching the other end of the remnant, you watch the wind fill it up and get an idea!")
    print('\n')
    use = input("Do you use the fabric to JUMP off the tower or WRAP around your shoulders for warmth? ")
    if use.upper() == "JUMP":
        jump()
    elif use.upper() == "WRAP":
        wrap()
    else: NonItem()

def bottle():
    RemoveFromBag ("BOTTLE")
    print("\n")
    print("Right as you grasp the small bottle, a bird swoops just overhead. ")
    print("With a start, you drop the bottle on the ruin grounds and it breaks!")
    print("You can’t help but hope that wasn’t going to come in handy later on.")
    print("\n")
    print("Well, what's left in your satchel? ")
    print(bag)
    use = input("Which one do you try next? ")
    if use.upper() == "TORCH":
        torch()
    elif use.upper() == "FABRIC":
        fabric()
    else: NonItem()

def torch():
    print("\n")
    print("Not sure how you're going to light it, you reach for the torch in your satchel.")
    print("WHOOSH!") 
    print("You suddenly feel the heat of a fire on your face.")  
    print("The torch lit itself as soon as it left the bag!")
    print("As you search the tower ruins, you don’t see much besides ")
    print("a walkway leading to another tower nearby and the crumbling remains of STAIRS")
    room = input("Do you go to the other TOWER or try going down the STAIRS? ")
    if room.upper == "STAIRS":
        lab()
    elif room.upper == "TOWER":
        tower()
    else: NonRoom()


"""ACTIONS"""

def jump():
    print("The castle grounds are slowly getting closer. ")
    print("As you glide above them, you can’t help but notice the gardens have ")
    print("obviously seen better days, but are still beautiful.")
    print("You’re in awe of the lush gardens until, suddenly, you hit the ground.")
    print("As you spit out the mouthful of grass, you get the eerie feeling someone is watching you. ")
    room = input(f">>{u}{i}SEARCH{clr}{i} the nearby ruins for a weapon or {u}EXPLORE{clr}{i} the gardens?{clr}")
    if room.upper == "SEARCH":
        ruins()
    elif room.upper == "EXPLORE":
        gardens()
    else: NonRoom()

def wrap():
    print("\n")
    print("Wow! This fabric is a lot thicker and more sturdy than it originally felt.")
    print("You look fabulous and feel nice and toasty. ")
    print("\n")
    print("What else looks useful in your satchel?")
    print(bag)
    use = input("What item do you try now? ")
    if use.upper == "FABRIC":
        fabric()
    elif use.upper == "TORCH":
        torch()
    elif use.upper == "BOTTLE":
        bottle()
    else: NonItem()


AddToBag ('FABRIC')
AddToBag ('TORCH')
AddToBag ('BOTTLE')

"""START"""
lab()


#____________________________________________
# notes:
#     start room:
#          BOTTLE working
#          TORCH working
#              - !!TOWER broken *prints NonItem
#              -!! STAIRS broken *prints NonItem
#          FABRIC working
#              - !!WRAP broken *works until you choose new item. Asks "What item do you try now?" upon entry, prints "What item do you want to use?"
#              - JUMP working
#                    + !!SEARCH broken *prints NonRoom
#                    + !!EXPLORE broken *prints Nonroom
#     lab:
#          TOES working
#          WATER working
#          SODA working
#               -SEARCH working
#               -!!EXPLORE working *Needs to be finished
#                   +!!MOAT broken *NOT YET ENTERED
#    tower: 
#          TAKE working
#          LEAVE working              
#               -!!JUMP broken *prints nonRoom
#               -!!STAIRS borken *prings NonRoom
#
#




 

print ("Inventory: ")
print (bag)
print("END OF FINISHED CODE!")
print("\n")


