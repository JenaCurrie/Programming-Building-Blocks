# While in the lab (access using "torch" then "stairs,") there is a hidden option! 
# You can type "all" to grab all items into your satchel. You greedy fella, you.

from os import system
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

def clear():
    _=system("cls")

"""to add to list"""
def AddToBag (item):
    bag.append (item)

"""to remove from list"""
def RemoveFromBag (item):
    bag.remove (item)

def CheckInventory():
    print(f"\n{clr}{i}Your bag has: ")
    print(*bag,sep=", ")
    
    

def NonRoom():
    room = input(f"{clr}{u}Where do you want to go?{clr} {think}")
    if room.upper() == "STAIRS":
        lab()
    elif room.upper() == "TOWER":
        tower()
    elif room.upper() == "SEARCH":
        ruins()
    elif room.upper() == "EXPLORE":
        gardens
    elif room.upper() == "PATH":
        shack()
    elif room.upper() == "MOAT":
        moat()
    else: moat()

def NonItem():
    CheckInventory()
    use = input(f"{clr}{u}What item do you want to use?{clr} {think}")
    if use.upper() == "TORCH":
        torch()
    elif use.upper() == "FABRIC":
        fabric()
    elif use.upper() == "BOTTLE":
        bottle()
    else: print(f"{clr}Can't seem to find a use for that item.{NonItem()}") 
        

"""ROOMS"""
    
def start():
    clear()
    print(f"{grock}{i}{name.upper()}{clr}{grock}!! Why, that's gotta be the best name I ever heard!")
    print(f"I'm {b}{i}Grock{clr}{grock}. But there's no time for pleasentries,")
    print(f"the sun's about teh start risin' so you've gotta git goin'!")
    print(f"{clr}His eyes drop to your hip")
    print(f"{grock}I see Princess Etheria's bag decided teh show itself to yeh.{clr}")
    print(f"{think}{i}    ...what bag is he talking about? I don't carry a--Wha-where did this satchel come from?!")
    print(f"    None of this makes sense{clr}")
    print(f"{think}Sorry, but who's Princess--{clr}{grock}I SAID THERE'S NO TIME! Now pick an item from the bag and GIT GOIN!")
    print(f"I'll catch up with yeh later. I have teh tell {i}Astral{clr}{grock} yer finally here!{clr}\n")
    
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
    clear()
    print(f"{think}{i}    slow...careful...*whew* I can't believe I made it all the way down!{clr}\n")
    
    print(f"You look around as you set your torch into a sconce.")
    print(f"{think}{i}    what is this room? It looks like an old Apothecary lab...{clr}")
    print("The light reveals a shelf nearby and the oddly shaped jars catch your eye.")
    print(f"{think}{i}    I should take something just in case, but I don't want my bag to get too heavy\n")
    print(f"    I'll just take one...let's see...Squid {u}TOES{clr}{think}, {i}Powdered {u}WATER{clr}{think} and {i}Baking {u}SODA.{clr}")
    take = input(f">> {u}Which do you take?{clr}{think} ")
    clear()
    if take.upper() == "TOES":
        AddToBag ("SQUID_TOES")
    elif take.upper() == "WATER":
        print(f"{think}{i}    How do you powder water? ...this bottle is empty.{clr}")
        print("You think you hear something and in a panic, you put the empty BOTTLE in your bag")
        AddToBag ("BOTTLE")
    elif take.upper() == ("SODA"):
        AddToBag ("BAKING_SODA")
    elif take.upper() == ("ALL"):
        print(f"\n{think}{i}    aw heck, why not take 'em all?!{clr}")
        AddToBag("WATER")
        AddToBag("POWDERED_WATER")
        AddToBag("BAKING_SODA")
    else: 
        print("You think you hear something and in a panic, you grab the BAKING SODA")
        AddToBag ("BAKING_SODA")
    CheckInventory()
    
    print(f"\nAs you're putting {i}{take.upper()}{clr} in your bag, You look over your shoulder ")
    print("toward shadows you hadn't noticed before.")
    print(f"   {think}{i}It's twilight. Grock said I need to figure this out before dawn.")
    print("    Is that the castle yards?{clr}")
    print("You grab the TORCH, put it back in your bag and walk out the crumbling doorway.\n")
    print("Suddenly, you get the eerie feeling someone is watching you.")
    room = input (f">> {u}Do you want to {i}SEARCH{clr}{u} the ruins for a weapon or {i}EXPLORE{clr}{u} the gardens?{clr}{think} ")
    if room.upper() == "SEARCH":
        ruins()
    elif room.upper() == "EXPLORE":
        gardens()
    else: NonRoom()
    
def tower():
    print(f"\n{clr}As you're walking down the rampart, you observe the wreckage around you.")
    print(f"You reach the other tower. {think}{i}   ...a bedroom?{clr}")
    print(f"You lift the torch to shed light on a portrait.\n")
    print(f"{gold}{i}Princess Etherea Chimericus: Keeper of the Dreams{clr}\n") 
    print("As you wonder what all this means, your gaze drops to the ground.")
    print(f"On the ruin ground, just in front of your foot, your eyes catch the glint of a gold coin. {clr}")
    take = input(f">> {u}Do you want to {i}TAKE{clr}{u} the coin or {i}LEAVE{clr}{u} it there?{clr}{think} ")
    if take.upper() == "TAKE":
        AddToBag ("GOLD_COIN")
        CheckInventory()
    else:
        print(f"{think}{i}    I should leave things alone...")
    print(f"{clr}\nSuddenly, you remember the fabric in your bag and get an idea!")
    use = input (f"{u}Do you use the fabric to {i}JUMP{clr}{u} or go back and use the {i}STAIRS{clr}?{think} ")
    if use.upper()== "JUMP":
        jump()
    elif use.upper()== "STAIRS":
        lab()
    else: NonRoom()

def ruins():
    clear()
    print(f"{clr} {i}WOOSH{clr}\n")
    print(f"The magic torch lights itself as you pull it out of the satchel.\n")
    print(f"Leading with the torch to ward off anyone (or any{i}thing{clr}) from approaching you, you step to the ruins.")
    print("Trying to make as little noise as possible, you carefully turn over the large stones that were once fortress walls.")
    print("Out of the corner of your eye, you see the light of your torch reflecting back at you.\n")
    print(f"{think}{i}    {u}A SWORD!{clr}")
    print("Somehow it fits into your new magic satchel and you feel much safer going on to explore the gardens.")
    AddToBag("SWORD")
    CheckInventory()

    print(f"\nBehind you, you notice a {u}MOAT.{clr}")
    room = input (f">> {u}Do you want to walk to the {i}MOAT{clr}{u}, go toward the drawbringe {i}PATH{clr}{u} or {i}EXPLORE{clr}{u} the gardens?{clr}{think} ")
    if room.upper() == "MOAT":
        moat()
    elif room.upper() == "EXPLORE":
        gardens()
    elif room.upper() == "PATH":
        path()
    else: NonRoom()

def moat():
    clear()
    print(f"\n{clr}{think}{i}    ...Something is making ripples in the water...what's in there?")
    print(f"{clr}As you step closer to the water, the ripples stop.")
    print(f"{think}{i}    I should see if something in my bag looks useful.")
    if "SWORD" in bag:
        print(f"{clr}Keeping your eyes on the water, you reach into your satchel.\n")
        print(f"You feel the {i}{u}TORCH{clr} and the {i}{u}SWORD.{clr}")
        squid = input(f">> {u}Use {i}TORCH{clr}{u}, {i}SWORD{clr}{u} or {i}RUN?{clr}{think} ")
        if squid.upper() == "TORCH":
            torch_squid()
        elif squid.upper() == "SWORD":
            sword_squid()
        elif squid.upper() == "RUN":
            print(f"{think}{i}    NOPE! SO MUCH NOPE!")
            print(f"{clr}You sprint toward the drawbridge {i}PATH{clr} to find a way out.")
            shack()
        else : 
            print(f"{think}{i}    NO WAY am I meeting whatever is living in there!{clr}")
            print(f"You run toward the drawbridge {i}PATH{clr} to the east")
            shack()
    else:    
        print(f"\n{clr}Keeping your eyes on the water, you reach into your satchel.")
        print(f"All you feel is the {i}{u}TORCH{clr}")
        squid = input(f"> {u}Do you pull out the {i}TORCH{clr}{u} or {i}RUN{clr}{u}?{clr} {think}")
        if squid.upper() == "TORCH":
            torch_squid()
        elif squid.upper() == "RUN":
            shack()

def gardens():
    clear()
    print(f"\n{clr}At a loss for what to do, you start walking around the gardens.")
    print(f"{think}{i}    a campfire pit! It's so cold out here, I can use my torch to light a fire and warm up!")
    print(f"{clr} As you get closer to the fire, you notice something that makes you feel uneasy." )
    print(f"{think}{i}    ...glowing embers?{clr}{think} There's someone here.{clr}\n")
    print(f"{pensive}Yes there is. Someone who needs you to continue your journey, {name.capitalize()}.\n")
    print(f"{clr} Startled to hear your name from an unfamiliar deep growl, you spin around")
    print(f"{think}{i}    HE'S HUGE! ...dirty...tired...hardened...intimidating but seems harmless...{clr}\n")
    print(f"{think}What journey?! I don't even know how I got here!{clr}")
    print(f"{pensive}I'd rather not make friends right now. Last time we welcomed a visitor, she did {i}this{clr}{pensive} to our kingdom")
    print(f"{clr}His eyes fall to the satchel on your hip and you see his whole face soften up") 
    print(f"{pensive}Here, take this. Just leave me be, please. If you need information, go see Astral.{clr}\n")
    print("As you take the GOLD COIN he hands you, you look behind you to follow the dismissive wave of his hand.")
    AddToBag("GOLD_COIN")
    print(f"You see a {i}{u}MOAT{clr} and the drawbridge {i}{u}PATH{clr}")
    room = input(f">> {u}Where do you go?{clr} {think}")
    if room.upper() == "MOAT":
        moat()
    elif room.upper() == "PATH":
        path()

def path():
    clear()
    print(f"{clr}{grock} 'OY! {name.upper()}!{clr}")
    print(f"{think}GROCK! You scared me! Can you tell me what I'm supposed to be doing now?{clr}\n")
    print(f"{grock}I wish I 'ad more answers fer yeh, {name.capitalize()}.")
    print(f"{grock}I told Astral yer here, ")
    print(f"{grock}but all she'd tell me was teh make sure yeh see the MOAT before yeh go see 'er. ")
    print(f"I mean, sure it's a beautiful MOAT 'n all, but I dun' know why she'd want yeh sight-seein' right now.\n")
    print(f"Anyway, I gotta go check on King Pensive. He's not been takin' care of 'imself so good lately.")
    print(f"Good luck, {name.capitalize()}! I know yeh can do this!{clr}\n")
    print(f"{think}{i}    The MOAT looks ominous, not beautiful. Why would I need to go look at it?{clr}\n")
    room = input(f">> {u}Do you conintue to the {i}PATH{clr}{u}, or go see the {i}MOAT{clr}? {think}")
    if room.upper() == "PATH":
        shack()
    elif room.upper() == "MOAT":
        moat()
    else:
        NonRoom()

def shack():
    clear()
    print(f"\n{clr}As you approach the drawbridge, you see an old, dilapidated shack come into view.")
    print(f"You cautiously approach the remains of what was once a doorway.\n")
    room = input (f">> {u}ENTER? (Y/N){clr} {think}")
    if room.upper() in "NO" "N":
        print(f"{clr}Just as you're about to turn away, you hear a frail, unfamiliar voice.")
    print(f"{astral}{name.capitalize()}, You've finally made it.{clr}")
    print(f"As you step further into the dilapidated shack, you see the dull twilight reveal a small figure in the corner.")
    print("Her back is toward you, but this isn't the wierdest thing that's happened today, so you answer her.\n")
    print(f"{think}I guess so? Where am I? How did I get here?...and how do I get home?{clr}")
    print("-------------------------------------------------------------")
    print(f"{astral}Oh, {name.capitalize()}. That's a long story.")
    story = input(f">> {u}Are you sure you want to hear the whole thing?{clr} {i}{u}YES{clr}{i} or {u}NO{clr} {think}")
    if story.upper() in "Y" "YES":
        clear()
        print(f"{astral}I like a hero who cares. Take a {i}GOLD COIN{clr}{astral} off that table for your kindness.\n")
        AddToBag ("GOLD_COIN")
        
        print(f"{astral}     I'm sure if you came across King Pensive on your journey, he didn't tell you anything, huh?") 
        print(f"     I wouldn't think so.  He’s been very elusive since Princess Etherea left, just sits in the garden by the fire all day stuck in his thoughts.")
        print(f"     Although he would have known that his daughter's satchel would only present to the one true hero.") 
        print(f"\n{clr}She slowly turns her tiny, worn body toward you and continues:")
        print(f"{astral}     See, {name.capitalize()}, about 300 years ago, a visitor came to Lunashire.  ") 
        print(f"     King Pensive loved his kingdom and was always willing to help his citizens.  ") 
        print(f"     She said she wasn’t a citizen of Lunashire, but needed the Princess’s help. ") 
        print(f"     She was an evil woman who wasn’t satisfied just taking away Princess Etherea’s sacred right to distribute dreams to the kingdom, ") 
        print(f"     she also had to take the princess with her.  ") 
        print(f"     Without Etherea’s dreams, we have been stuck in perpetual cognizance for 300 years. \n") 
    elif story.upper() in "N" "NO":
        clear()   
    print(f"{astral}Now {name.capitalize()}, I'm sure you'd like to get home. ")
    print(f"I know it may sound odd, but you need to make a {pie}Dream Cream Pie{clr}{astral} before dawn today")
    print(f"to restore our ability to sleep and allow time to continue turning here in Lunashire.")
    print(f"Without the Princess' satchel, we have been unable to harvest all the ingredients needed for the {pie}Dream Cream Pie{clr}")
    print(f"{astral}Now that Etheria's satchel chose you, you had all the tools to harvest the ingredients. ")
    print(f"But to free us from this curse, the {pie}Dream Cream Pie {clr}{astral}has to be made before the dawn of the ")
    print(f"morn marking exactly 300 years since the Princess disapeared.")
    print(f"I'm sure you've gathered...when the sun rises today, it will be exactly 300 years.{clr}\n")
    
    recipe = input(f">> {u}{i}ASK{clr}{u} for the recipe or {i}CHECK{clr}{u} your bag for ingredients?{clr} {think}")
    clear()
    if recipe.upper() == "ASK":
        title = f"{pie}Dream Cream Pie"
        line_one = f"{pie}3 Squid Toes"
        line_two = f"{pie}1palm Powdered Water"
        line_three = f"{pie}1pinch Baking Soda"
        line_four = f"{pie}  >Mix ingredients until Squid Toes are almost mush"
        line_five = f"{pie}  >Pour near-mush mixture into a pan"
        line_six = f"{pie}  >Hold the Lunashire Magic Flame over mixture for 5 minutes"
        fill = f"{pie}"  
        print(f"{clr}Astral hands you a piece of parchment with a recipe on it")         
        print(title.center(75,"-"))
        print(line_one.center(75))
        print(line_two.center(75))
        print(line_three.center(75))
        print(line_four.ljust(75))
        print(line_five.ljust(75))
        print(line_six.ljust(75))
        print(fill.center(75,"-"))
    
    print(f"\n{astral}Let's see how many ingredients you were able to collect on your way here.{clr}")
    show_ingredients = input(f"{clr}>> {u}Show Astral inside your bag? {i}Y/N:{clr}{think}  ")
    if show_ingredients.upper == "YES" or "Y":
        clear()
        CheckInventory()
        if "POWDERED_WATER" in bag: 
            if "SQUID_TOES" in bag and "BAKING_SODA" in bag:
                print(f"{astral}AH, YES! {name.upper()}! YOU WERE ABLE TO HARVEST THE POWDERED WATER!")
                print(f"{astral}Only the flame of Princess Etheria's magic torch can powder the water shed from the Great Lunashire Phalange Squid.")
                print(f"{astral}Let's start baking!")
                montage()
            elif (("SQUID_TOES" not in bag and "BAKING_SODA" not in bag) and bag.count("GOLD_COIN") <=1) or (("SQUID_TOES" not in bag or "BAKING_SODA" not in bag) and bag.count("GOLD_COIN") <1) :
                print(f"{astral}I see you're still missing some of the other ingredients.")
                print(f"I have some extras in that coin machine but you don't have enough GOLD COINS for both ingredients!\n")
                fail_1()
            elif ("SQUID_TOES" not in bag or "BAKING_SODA" not in bag) and bag.count("GOLD_COIN") >=1 :
                print(f"{astral}Oh good! I see you have enough coins for your missing ingredient!")
                print(f"{clr}You head over to the coin machine with the ingredient you're missing and put in your coin")
                print(f"The vial falls to the bottom and you lift the flap to get it out")
                RemoveFromBag ("GOLD_COIN")
                montage()
            elif bag.count("SQUID_TOES" "BAKING_SODA") <1 and bag.count("GOLD_COIN") >=2:
                print(f"{astral}Oh good! I see you have enough coins for your missing ingredient!")
                print(f"{clr}You head over to the coin machine with the ingredient you're missing and put in your coin")
                print(f"The vial falls to the bottom and you lift the flap to get it out")
                RemoveFromBag ("GOLD_COIN")
                RemoveFromBag ("GOLD_COIN")
                montage()
        elif "POWDERED_WATER" not in bag:
            print(f"{astral}Oh, {name.upper()}! You don't have any POWDERED WATER! That was the one ingredient I can't help you with.")
            fail_1()   
    else:
        fail_2()

"""ITEMS"""

def fabric():
    clear()
    print(f"{clr}You unfold the large piece of fabric. \nAs you’re examining it, the wind catches it and nearly blows it out of your hand.")
    print("Quickly catching the other end of the remnant, you watch the wind fill it up and get an idea!\n")
    use = input(f">> {u}Do you use the fabric to {i}JUMP{clr}{u} off the tower or {i}WRAP{clr}{u} around your shoulders for warmth?{clr} {think} ")
    if use.upper() == "JUMP":
        jump()
    elif use.upper() == "WRAP":
        wrap()
    else: NonItem()

def bottle():
    clear()
    RemoveFromBag ("BOTTLE")
    print(f"\n{clr}Right as you grasp the small bottle, a bird swoops just overhead.")
    print(f"{think}AH!{clr} {i}*CRASH*{clr} you look down and see...")
    print(f"{think}{i}    Welp...I hope that bottle wasn’t going to come in handy later on.\n")
    print(f"    What's left in this satchel? {clr}")
    print(*bag,sep=", ")
    use = input(f"{clr}>> {u}Which one do you try next?{clr} {think}")
    if use.upper() == "TORCH":
        torch()
    elif use.upper() == "FABRIC":
        fabric()
    else: NonItem()

def torch():
    clear()
    print(f"{clr}Not sure how you're going to light it, you reach for the torch in your satchel.")
    print(f"\n{i}WHOOSH!{clr}\n") 
    print(f"{think}{i}    ...My cheek is so warm...")  
    print(f"{think}{i}    A magic TORCH!?{clr}")
    print("\nAs you search the tower ruins, you don’t see much besides ")
    print("a walkway leading to another tower nearby and the crumbling remains of STAIRS\n")
    room = input(f">> {u}Do you go to the other {i}TOWER{clr}{u} or try going down the {i}STAIRS?{clr} {think}")
    if room.upper()== "STAIRS":
        lab()
    elif room.upper()== "TOWER":
        tower()
    else: NonRoom()

def torch_squid():
    clear()
    print(f"\n{clr}Holding the torch in front of you, you lean over the still water.")
    print(f"{think}    ...whatever was there must have been scared off by my approach to the water...{clr}")
    print(f"Just as you’re about to turn away, a ginormous squid leaps out of the water toward you!")
    print(f"")
    print(f"Panicked, all you can think to do is to reach the torch up to his smooth, slimey body. ")
    print(f"He let out the most bazaar {squid}{i}YELP{clr} you've ever heard")
    print(f"As he landed back in the water, you watched him race away toward the dim twilight. ")
    print(f"\nRecalling what looked like snow falling from the scorched squid, you look down at your feet.")
    if "BOTTLE" in bag:
        print(f"{think}{i}    ...What is this?! ")
        print(f"{clr}You remember the {u}BOTTLE{clr} in your bag.")
        powder = input(f">> {clr}{u}Do you scoop the powder into your {i}BOTTLE{clr}{u} or {i}RUN{clr}{u} far far away?{clr} {think}")
        if powder.upper() == "BOTTLE":
            print(f"    What the heck is this stuff?")
            print(f"{clr}You scoop as much of the ...wet...(?) powder as you can into the bottle.")
        AddToBag ("POWDERED_WATER")
        CheckInventory()
    if "BOTTLE" not in bag:
        print(f"{think}{i}    ...I bet that broken bottle would have come in handy right about now.")
    print(f"{clr}Wanting to get away from the water, you run toward the drawbridge PATH")
    shack()

def sword_squid():
    clear()
    print(f"\n{clr}Holding the SWORD in front of you, you lean over the still water.")
    print(f"{think}    ...whatever was there must have been scared off by my approach to the water...{clr}")
    print(f"Just as you’re about to turn away, a ginormous squid leaps out of the water toward you!\n")
    print(f"Panicked, all you can think to do is to swing the sword at his smooth, slimey body. \n")
    print(f"He let out the most bazaar {squid}{i}YELP{clr} you've ever heard")
    print(f"as a tentacle {squid}*SQUISH PLOP*{clr}PED at your feet\n")
    print(f"As he landed back in the water, you watched him race away toward the sunrise as he grew another tenticle ")
    print("You look down at the ground and can't help but laugh")
    print(f"{think}{i}    Is that...TOES on these tentacles?!")
    take = input (f"{clr}>> {u}Take the {i}SQUID TOES{clr}{u}?(Y/N){clr} {think}")
    if take.upper() == "Y" "YES" "TOES":
        clear()
        print(f"    I have to take these to show my friends when I get home.{clr}")
        AddToBag ("SQUID_TOES")
        CheckInventory()
    else:
        clear()
        print(f"{clr}You leave the nasty, slimey toes...but you can't help taking a closer look")
    print(f"\nYou pull out the torch to get a better look at the toed tentacle.")
    print(f"As you move the flame closer, you see some water instantly turn into a wierd powder.")
    if "BOTTLE" in bag:
        print(f"{think}{i}    ...What is this?! ")
        print(f"{clr}You remember the {u}BOTTLE{clr} in your bag.")
        powder = input(f">> {clr}{u}Do you scoop the powder into your {i}BOTTLE{clr}{u} or {i}RUN{clr}{u} far far away?{clr} {think}")
        if powder.upper() == "BOTTLE":
            print(f"    What the heck is this stuff?")
            print(f"{clr}You scoop as much of the ...wet...(?) powder as you can into the bottle.\n")
            AddToBag ("POWDERED_WATER")
            CheckInventory()
            print(f"\n{think}{i}    I need to figure out how to get home.")
            print(f"    let's walk toward the drawbridge to see what's over there.{clr}")
            room = input (f">> {u}Walk to the drawbridge PATH?{clr}(Y/N) {think}")
            if room.upper() == "Y" "YES" "PATH":
                shack()
            else:
                NonRoom()
    elif "BOTTLE" not in bag:
        print(f"{think}{i}    ...I bet that broken bottle would have come in handy right about now.")
        print(f"{think}{i}    I need to figure out how to get home.")
        print(f"    let's walk toward the drawbridge to see what's over there.{clr}")
        room = input (f">> {u}Walk to the drawbridge PATH?{clr}(Y/N) {think}")
        if room.upper() == "Y" "YES" "PATH":
           shack()
        else:
           NonRoom()

"""ACTIONS"""

def jump():
    clear()
    print(f"{clr}{think}{i}    This fabric catches the wind so well! ...If Link can do it...?")
    print(f"{clr}Holding on tight to two corners, you hold the fabric above your head and JUMP.\n")
    print(f"{think}{i}   The castle grounds are slowly getting closer. ")
    print(f"{think}{i}   The gardens have obviously seen better days, but they're still gorgeous.")
    print(f"{clr}You’re in awe of the lush gardens until, suddenly, you hit the ground.\n")
    print(f"As you spit out the mouthful of grass, you get the eerie feeling someone is watching you. ")
    room = input(f">> {u}{i}SEARCH{clr}{u} the nearby ruins for a weapon or {i}EXPLORE{clr}{u} the gardens?{clr} {think}")
    if room.upper()== "SEARCH":
        ruins()
    elif room.upper()== "EXPLORE":
        gardens()
    else: NonRoom()

def wrap():
    clear()
    print(f"\n{think}{i}    Wow! This fabric is a lot thicker and more sturdy than it originally felt.{clr}")
    print("What else looks useful in your satchel?")
    CheckInventory()
    use = input(f"{u}What item do you try now?{clr} {think}")
    if use.upper()== "FABRIC":
        jump()
    elif use.upper()== "TORCH":
        torch()
    elif use.upper()== "BOTTLE":
        bottle()
    else: NonItem()

"""ENDINGS"""

def fail_1():
    print(f"{name.capitalize()}, you've failed Lunashire.")
    print(f"And now it's too late because the sun rising!\n")
        
    print(f"{clr}Your heart starts beating faster as you think of the people of Lunashire")
    print(f"being stuck for another 300 years waiting for a hero who WON'T fail them.\n")
    print(f"{think}I'm sorry! I didn't know what to do!")
    print(f"{i}     ... I didn't know what to do!...{clr}")
    print(f"{think}ASTRAL!")
    print(f"{clr}She's fading from your view as you beg her not to leave.")
    print(f"{think}{b}ASTRAL!")
    print(f"{clr}You notice your voice was clearer than it was before. Closer.")
    print(f"You look around and notice you're in your own bed, laying on your own pillow.")
    print(f"{think}{i}{b}What a bazaar dream.\n")

def fail_2():
    clear()
    print(f"{astral}Oh, {name.upper()}! I should have known better than to trust you!")
    print(f"{name.upper()}, YOU WERE WORKING FOR THAT HORRID WOMAN ALL ALONG, WHEREN'T YOU!?\n")
        
    print(f"{clr}Astral turns her back toward you and picks something up off the table behind her")
    print(f"{think}AStral! I didn't ask for this. I just want to get home!")
    print(f"{astral}Dear, you're never going home now.\n")
    print(f"{clr}Suddenly, you see a BRIGHT flash.")
    print(f"{clr}Astral is growing taller! Leaning over you...claws growing from her fingers and fangs in her mouth.")
    print(f"{think}{b}ASTRAL!")
    print(f"{clr}You notice your voice was clearer than it was before. Closer.")
    print(f"You look around and notice you're in your own bed, laying on your own pillow.")
    print(f"{think}{i}{b}What a bazaar dream.\n")

def montage():
    print(f"{pie}------*QUE MONTAGE*------")
    print(f"-----------------------------------")
    print(f"    {i}....gather ingredients....")
    print(f"    ....make squid toes dance....")
    print(f"    ....heartfelt conversation....")
    print(f"    ....frollic through gardens in slow motion....{clr}\n")
    print(f"{astral}{name.capitalize()}?...{name.upper()}?...{name.upper()}!{clr}")
    print(f"{think}WHAT!? ...oh is it done!?")
    print(f"{astral}It's finished, {name.capitalize()}. Now the hero needs to take a bite before sunrise")
    print(f"So we can all be free and you can go home!")
    end = input (f"{clr}>> {u}Do you {i}EAT{clr}{u} the pie or {i}REFUSE?{clr} {think}")
    if end.upper() == "EAT":
        end_win()
    elif end.upper() == "REFUSE":
        fail_2()
    else:
        end_win()

def end_win():
    clear()
    print(f"{clr}{think}{i}    I know what ingredients went into this pie...there's no way it smells this good!\n")
    print(f"{clr}You lean over the warm, whipped, creamy pie and take the biggest bite possible")
    print(f"    {i}You close your eyes in complete bliss")
    print(f"    {i}This is the best thing you've ever tasted!")
    print(f"You take a deep breath to savor the last moment before you swallow.")
    print(f"As your eyes open, you look around and notice you're in your own bed, laying on your own pillow.\n")
    print(f"{think}    ...What a bazaar dream...\n")
    print(f"{clr}You get up to go to the bathroom.")
    print(f"As you pass by the mirror, you notice something...")
    print(f"{think}{i}    Is that...whipped pie on my face??")
    print(f"{clr}You instictively reach into your pajama pockets and feel...")
    print(f"{think}{i}   ...{bag.count('GOLD_COIN')} gold coins!")



AddToBag ('FABRIC')
AddToBag ('TORCH')
AddToBag ('BOTTLE')

"""START"""

clear()
print(f"{think}{i}    ...ouch...my head...everything is blurry...")
print(f"    ...am I...in a castle tower? Why am I laying on all this rubble...{clr}\n")

print(f"{grock}OH 'EY THERE, LITTLE FELLER!")
print(f"I DIDN'T THINK YEH'D EVER WAKE UP!")
print(f"We don't get many outsiders visitin' Lunashire anymore.")
name = input(f">> {u}Can I ask ye what yur name is, feller?{clr}{think} ")
if name.upper() in "Y"  "YES"  "SURE":      #Watching my dad try to play through alerted me to this necessary option...
    print(f"{clr}{grock}\nHA, got a bit of a sense o' humor, don'tcha?")
    name = input(f">> {u}What should I call yah?{clr}{think} ")
start()
