# While in the lab (access using "torch" then "stairs,") there is a hidden option! 
# You can type "all" to grab all items into your satchel. You greedy fella, you.

bag=[]

u = "\033[4m"
b = "\033[1m"
i = "\033[3m"
think = "\033[38;5;111m"
grock = "\033[38;5;48m"
pensive = "\033[38;5;166m"
astral = "\033[38;5;212m"
gold = "\033[38;5;136m"
pie = "\033[38;5;5m\033[3m"
squid= "\033[38;5;57m"
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
    print(f"{grock}{name.upper()}!! Why, that's gotta be the best name I ever heard!")
    print(f"I'm {b}{i}Grock{clr}{grock}. But there's no time for pleasentries, ")
    print(f"the sun's about teh start risin' so you've gotta git goin'!")
    print(f"I see Princess Etheria's bag decided teh show itself to yeh.{clr}")
    print(f"{think}{i}    ...what bag is he talking about? I don't have a--Wha-where did this satchel come from?!")
    print(f"None of this makes sense{clr}")
    print(f"{think}Sorry, but who's Princess--{clr}{grock}I SAID THERE'S NO TIME! Now pick an item from the bag and GIT GOIN!")
    print(f"I'll catch up with yeh later. I have teh tell {i}Astral{clr}{grock} yer finally here!{clr}")
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
    line()
    print(f"{think}{i}    slow...careful...*whew* I can't believe I made it all the way down!{clr}")
    line()
    print(f"You look around as you set your torch into a sconce.")
    print(f"{think}{i}    what is this room? It looks like an old Apothecary lab...{clr}")
    print("The light reveals a shelf nearby and the oddly shaped jars catch your eye.")
    print(f"{think}{i}    I should take something just in case, but I don't want my bag to get too heavy")
    line()
    print(f"    I'll just take one...let's see...Squid {u}TOES{clr}{think}, {i}Powdered {u}WATER{clr}{think} and {i}Baking {u}SODA.{clr}")
    take = input(f">>{u}Which do you take?{clr}{think} ")
    if take.upper() == "TOES":
        AddToBag ("SQUID_TOES")
    elif take.upper() == "WATER":
        print(f"{think}{i}    How do you powder water? ...this bottle is empty.{clr}")
        print("You think you hear something and in a panic, you put the empty BOTTLE in your bag")
        AddToBag ("BOTTLE")
    elif take.upper() == ("SODA"):
        AddToBag ("BAKING_SODA")
    elif take.upper() == ("ALL"):
        line()
        print(f"{think}{i}    aw heck, why not take 'em all?!{clr}")
        AddToBag("WATER")
        AddToBag("POWDERED_WATER")
        AddToBag("BAKING_SODA")
    else: 
        print("You think you hear something and in a panic, you grab the BAKING SODA")
        AddToBag ("BAKING_SODA")
    CheckInventory()
    line()
    print(f"As you're putting {i}{take.upper()}{clr} in your bag, You look over your shoulder toward a dull, orange glow.")
    print(f"   {think}{i}the sun is coming up. Is that the castle yards?{clr}")
    print("You grab the TORCH, put it back in your bag and walk out the crumbling doorway.")
    line()
    print("Suddenly, you get the eerie feeling someone is watching you.")
    room = input (f">>{u}Do you want to {i}SEARCH{clr}{u} the ruins for a weapon or {i}EXPLORE{clr}{u} the gardens?{clr}{think} ")
    if room.upper() == "SEARCH":
        ruins()
    elif room.upper() == "EXPLORE":
        gardens()
    else: NonRoom()
    
def tower():
    print(f"{clr}As you're walking down the rampart, you observe the wreckage around you.")
    print(f"You reach the other tower. {think}{i}   ...a bedroom?{clr}")
    print(f"You lift the torch to shed light on a portrait.")
    line()
    print(f"{gold}{i}Princess Etherea Chimericus: Keeper of the Dreams{clr}") 
    line()
    print("As you wonder what all this means, your gaze drops to the ground.")
    print(f"On the ruin ground, just in front of your foot, your eyes catch the glint of a gold coin. {clr}")
    take = input(f">>{u}Do you want to {i}TAKE{clr}{u} the coin or {i}LEAVE{clr}{u} it there?{clr}{think} ")
    if take.upper() == "TAKE":
        AddToBag ("GOLD_COIN")
        CheckInventory()
    else:
        print(f"{think}{i}    I should leave things alone...")
    line()
    print(f"{clr}Suddenly, you remember the fabric in your bag and get an idea!")
    use = input (f"Do you use the fabric to {i}{u}JUMP{clr} or go back and use the {i}{u}STAIRS{clr}?{think} ")
    if use.upper()== "JUMP":
        jump()
    elif use.upper()== "STAIRS":
        lab()
    else: NonRoom()

def ruins():
    line()
    print(f"Leading with the torch to ward off anyone (or any{i}thing{clr}) from approaching you, you step to the ruins.")
    print("Trying to make as little noise as possible, you carefully turn over the large stones that were once fortress walls.")
    print("Out of the corner of your eye, you see the light of your torch reflecting back at you.")
    line()
    print(f"{i}A sword!{clr}")
    print("Somehow it fits into your new magic satchel and you feel much safer going on to explore the gardens.")
    AddToBag("SWORD")
    line()
    print("Behind you, you notice a MOAT.")
    room = input (f"{u}Do you want to walk to the {i}MOAT{clr}{u} or {i}EXPLORE{clr}{u} the gardens?{clr}{think} ")
    if room.upper() == "MOAT":
        moat()
    elif room.upper() == "EXPLORE":
        gardens()
    else: NonRoom()

def moat():
    line()
    print(f"{clr}{think}{i}    ...Something is making ripples in the water...what's in there?")
    print(f"{clr}As you step closer to the water, the ripples stop.")
    print(f"{think}{i}    I should see if something in my bag looks useful.")
    if "SWORD" in bag:
        print(f"{clr}Keeping your eyes on the water, you reach into your satchel.")
        print(f"You feel the {i}{u}TORCH{clr} and the {i}{u}SWORD.{clr}")
        squid = input(f">>{u} Which do you pull out?{clr}{think} ")
        line()
        if squid.upper() == "TORCH":
            torch_squid()
        elif squid.upper() == "SWORD":
            sword_squid()
        else : 
            print(f"{think}{i}    NO WAY am I meeting whatever is living in there!{clr}")
            print(f"You run toward the drawbridge {i}PATH{clr} to the east")
            shack()
    else:    
        print(f"{clr}Keeping your eyes on the water, you reach into your satchel.")
        print(f"You feel the {i}TORCH{clr} and pull it out")
        torch_squid()

def gardens():
    line()
    print(f"{clr}Leading with the torch to ward off anyone (or any{i}thing{clr}) from approaching you, you step further into the gardens.")
    print(f"{think}{i}    a campfire pit! It's so cold out here, I can use my torch to light a fire and warm up!")
    print(f"{clr} As you get closer to the fire, you notice something that makes you feel uneasy." )
    print(f"{think}{i}    ...glowing embers?{clr}{think} Someone is here.{clr}{pensive}")
    line()
    print(f"{pensive}Yes there is. Someone who needs you to continue your journey, {name.capitalize()}.")
    line()
    print(f"{clr} Startled to hear your name from an unfamiliar deep growl, you spin around")
    print(f"{think}{i}    HE'S HUGE! ...dirty...tired...hardened...intimidating but seems harmless...{clr}")
    print(f"{think}Where am I? I don't know what journey I'm even on!{clr}")
    print(f"{pensive}I'd rather not make friends right now. Last time we welcomed a visitor, she did {i}this{clr}{pensive} to our kingdom")
    print(f"{clr}His eyes fall to the satchel on your hip and you see his eyes soften up") 
    print(f"{pensive}Here, take this. Just leave me be, please. If you need information, go see Astral.{clr}")
    line()
    print("As you take the GOLD COIN he hands you, you look behind you to follow the dismissive wave of his hand.")
    AddToBag("GOLD_COIN")
    print(f"You see a {i}{u}MOAT{clr} and the drawbridge {i}{u}PATH{clr}")
    room = input(f">> {u}Where do you go?{clr} {think}")
    if room.upper() == "MOAT":
        moat()
    elif room.upper() == "PATH":
        shack()

def shack():
    line()
    print(f"{astral}{name.capitalize()}, You've finally made it.{clr}")
    print(f"{clr}As you step further into the dilapidated shack, you see the orange sunlight on a small figure in the corner.")
    print("Her back is toward you, but this isn't the wierdest thing that's happened today, so you answer her.")
    print(f"{think}I guess so? Where am I? How did I get here?...and how do I get home?{clr}")
    print("-------------------------------------------------------------")
    print(f"{astral}Oh, {name.capitalize()}. That's a long story.")
    story = input(f">> {u}Are you sure you want to hear the whole thing?{clr} {i}{u}YES{clr}{i} or {u}NO{clr} {think}")
    if story.upper() =="YES":
        print(f"{astral}I like a hero who cares. Take a {i}GOLD COIN{clr}{astral} for your kindness.")
        AddToBag ("GOLD_COIN")
        print(f"You see, {name.capitalize()}, {clr}")
        print(f"She slowly turns her worn body toward you and continues:")
        print(f"{astral}“I'm sure if you came across King Pensive on your journey, he didn't tell you anything, huh?") 
        print(f"I wouldn't think so.  He’s been very elusive since Princess Etherea left, just sits in the garden by the fire all day stuck in his thoughts.")
        print(f"Although he would have known that his daughter's satchel would only present to the one true hero.") 
        line()
        print(f"See, {name.capitalize()}, about 300 years ago, a visitor came to Lunashire.  ") 
        print(f"King Pensive loved his kingdom and was always willing to help his citizens.  ") 
        print(f"She said she wasn’t a citizen of Lunashire, but needed the Princess’s help. ") 
        print(f"She was an evil woman who wasn’t satisfied just taking away Princess Etherea’s sacred right to distribute dreams to the kingdom, ") 
        print(f"she also had to take the princess with her.  ") 
        print(f"Without Etherea’s dreams, we have been stuck in perpetual cognizance for 300 years. ") 
        line()
    print(f"{astral}Now {name.capitalize()}, I'm sure you'd like to get home. ")
    print(f"I know it may sound odd, you need to make a {pie}Dream Cream Pie{clr}{astral} to restore our ability to sleep and allow time to continue turning here in Lunashire.")
    print(f"Without the Princess' satchel, we have been unable to harvest all the ingredients needed for the {pie}Dream Cream Pie{clr}")
    print(f"Astral hands you a piece of parchment with a recipe on it")
    title = f"{pie}Dream Cream Pie"
    line_one = f"{pie}3 Squid Toes"
    line_two = f"{pie}1palm Powdered Water"
    line_three = f"{pie}1pinch Baking Soda"
    line_four = f"{pie}  >Mix ingredients until Squid Toes are almost mush"
    line_five = f"{pie}  >Pour near-mush mixture into a pan"
    line_six = f"{pie}  >Hold the Lunashire Magic Flame over mixture for 5 minutes"
    fill = f"{pie}"           
    print(title.center(75,"-"))
    print(line_one.center(75))
    print(line_two.center(75))
    print(line_three.center(75))
    print(line_four.ljust(75))
    print(line_five.ljust(75))
    print(line_six.ljust(75))
    print(fill.center(75,"-"))
    line()
    print(f"{astral}Let's see how many ingredients you were able to collect on your way here. Open your bag for me.{clr}")
    print(f"{clr}You show Astral inside your bag")
    CheckInventory()
    if "POWDERED_WATER" in bag:
        print(f"{astral}AH, YES! {name.upper()}! YOU WERE ABLE TO HARVEST THE POWDERED WATER!")
        print(f"{astral}Only the flame of Princess Etheria's magic torch can powder the water shed from the Great Lunashire Phalange Squid.")
    else:
        print(f"{astral}Oh, my. You don't have any POWDERED WATER!")
        print(f"{name.capitalize()}, you've failed Lunashire. That was the one ingredient I can't help you with.")
        line()
        print(f"{clr}Your heart starts beating faster as you think of the people of Lunashire")
        print(f"being stuck for another 300 years waiting for a hero who WON'T fail them.")
        line()
        print(f"{think}I'm sorry! I didn't know what to do!")
        print(f"{think}{i}     ... I didn't know what to do!...")
        print(f"{think}ASTRAL!")
        print(f"{clr}She's fading from your view as you beg her not to leave.")
        print(f"{think}{b}ASTRAL!")
        print(f"{clr}You notice your voice was clearer than it was before. Closer.")
        print(f"You look around and notice you're in your own bed, laying on your own pillow.")
        print(f"{think}{b}What a bizzar dream.")

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
    if room.upper()== "STAIRS":
        lab()
    elif room.upper()== "TOWER":
        tower()
    else: NonRoom()

def torch_squid():
    print(f"{clr}Holding the torch out in front of you, you pause at the moat’s edge as you notice the ripples suddenly stop.")
    print(f"{think}    whatever was there must have been scared off by my approach to the water.{clr}")
    print(f"Just as you’re about to turn away, ")
    print(f"a ginormous squid leaps out of the water toward you!")
    print(f"Panicked, all you can think to do is to reach the torch to his smooth body. ")
    print(f"\nHe let out the most bazaar {squid} YELP{clr} you've ever heard")
    print(f"As he landed back in the water, you watched him race away toward the sunrise. ")
    print(f"Recalling what seemed like snow falling from the scorched squid, you look down at your feet.")
    if "BOTTLE" in bag:
        print(f"{think}{i}    ...What is this?! ")
        print(f"{clr}You remember the bottle in your bag and scoop in as much of the powder as you can.")
        AddToBag ("POWDERED_WATER")
    if "BOTTLE" not in bag:
        print(f"{think}{i}    ...I bet that broken bottle would have come in handy right about now.")
    print(f"{clr}Wanting to get away from the water, you run toward the drawbridge PATH")
    shack()
def sword_squid():
    print(f"Holding the sword tight, you slowly walk closer to the water")


"""ACTIONS"""

def jump():
    print("The castle grounds are slowly getting closer. ")
    print("As you glide above them, you can’t help but notice the gardens have ")
    print("obviously seen better days, but are still beautiful.")
    print("You’re in awe of the lush gardens until, suddenly, you hit the ground.")
    print("As you spit out the mouthful of grass, you get the eerie feeling someone is watching you. ")
    room = input(f">>{u}{i}SEARCH{clr}{i} the nearby ruins for a weapon or {u}EXPLORE{clr}{i} the gardens?{clr}")
    if room.upper()== "SEARCH":
        ruins()
    elif room.upper()== "EXPLORE":
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
    if use.upper()== "FABRIC":
        fabric()
    elif use.upper()== "TORCH":
        torch()
    elif use.upper()== "BOTTLE":
        bottle()
    else: NonItem()


AddToBag ('FABRIC')
AddToBag ('TORCH')
AddToBag ('BOTTLE')

"""START"""
line()
print("--------------------------------------------------------------------------------------")
line()
print(f"{think}{i}    ...ouch...my head...everything is blurry...")
print(f"    ...am I...in a castle tower? Why am I laying on all this rubble...{clr}")
line()
print(f"{grock}OH 'EY THERE, LITTLE FELLER!")
print(f"I DIDN'T THINK YEH'D EVER WAKE UP!")
print(f"We don't get many outsiders visitin' Lunashire anymore.")
name = input(f">>{u}can I ask ye what yur name is, feller?{clr}{think} ")
line()
start()
