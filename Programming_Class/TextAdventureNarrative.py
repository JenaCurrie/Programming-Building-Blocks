bag=[]
u = "\033[4m"
b = "\033[1m"
i = "\033[3m"
think = "\033[38;5;111m"
grock = "\033[38;5;48m"
clr = "\033[0m"
def line():
    print("\n")

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
    line()
    print("--------------------------------------------------------------------------------------")
    line()
    print(f"{think}{i}...ouch...my head...everything is blurry...")
    print(f"...am I...in a castle tower? Why am I laying on all this rubble...{clr}")
    line()
    print(f"{grock}OH 'EY THERE, LITTLE FELLER!")
    print(f"I DIDN'T THINK YEH'D EVER WAKE UP!")
    print(f"We don't get many outsiders visitin' Lunashire anymore.")
    name = input(f">>can I ask ye what yur name is, feller?{clr}{think} ")
    line()
    print(f"{grock}{name.upper()}!! Why, that's gotta be the best name I ever heard!")
    print(f"{grock}I'm {b}{i}Grock{clr}{grock}. But there's no time for pleasentries, you've gotta git goin'!")
    print(f"I see Princess Etheria's bag decided teh show itsself to yeh.{clr}")
    line()
    print(f"{think}{i}bag? - Wha-where did this satchel come from?! None of this makes sense{clr}")
    print(f"{think}Sorry, but who's Princess--{clr}{grock}I SAID THERE'S NO TIME! Now pick an item from the bag and GIT GOIN!")
    print(f"I'll catch up with yeh later. I have teh tell Astral yer finally here!{clr}")
    line()
    print(f"You look into the bag and see a small corked {u}{i}BOTTLE{clr}, a large peice of {u}{i}FABRIC{clr} and a {u}{i}TORCH{clr}.")
    use = input(f">> {u}Which item do you pull out?{clr}{think} ")
    if use.upper() == "FABRIC":
        fabric()
    elif use.upper() == "BOTTLE":
        bottle()
    elif use.upper() == "TORCH":
        torch()
    else: NonItem()
        
def lab():
    print("\n")
    print(f"{think}{i}slow...careful...I can't believe I made it all the way down!{clr}")
    print("\n") 
    print(f"You look around as you set your torch into a sconce.")
    print(f"{think}{i} what is this room? an old Apothecary lab?{clr}")
    print("The light reveils a shelf nearby and the oddly shaped jars catch your eye.")
    print(f"{think}{i}I should take something in just in case, but I don't want my bag to get too heavy")
    print(f"...let's see...Squid {u}TOES{clr}{think}, {i}Powdered {u}WATER{clr}{think} and {i}Baking {u}SODA.{clr}")
    print("\n")
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
    print(f"{think}you notice an opening through which you can barely make out the shadows of grass")
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
    line()
    print(f"{clr}Right as you grasp the small bottle, a bird swoops just overhead.")
    print(f"{think}AH!{clr} {i}*CRASH*{clr} you look down and see...")
    print(f"{think}{i}Welp...I hope that bottle wasn’t going to come in handy later on.")
    print("What's left in this satchel? {clr}")
    line()
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
start()
