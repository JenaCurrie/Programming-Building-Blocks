bag=[]
"""to add to list"""
def AddToBag (item):
    bag.append (item)
"""to remove from list"""
def RemoveFromBag (item):
    bag.remove (item)

def CheckInventory():
    print("Your bag has:")
    print(bag)

def lab():
    print("You s.l.o.w.l.y and carefully start down the stairs.")
    print("Amazingly, you reach the bottom safely!") 
    print("Standing in what seems to be an old apothecary lab, you put your torch in a sconce nearby")
    print("\n")
    print("The oddly shaped jars catch your eye.")
    print("Scanning the shelf, you see a jars labeled Squid TOES, powdered WATER and baking SODA.")
    print("Not wanting to weigh down your satchel, you only want to take one bottle.")
    take = input("Which do you take? ")
    if take.upper() == "TOES":
        AddToBag ("SQUID_TOES")
    if take.upper() == "WATER":
        AddToBag ("POWDERED_WATER")
    if take.upper() == ("SODA"):
        AddToBag ("BAKING_SODA")

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
        use = input ("Do you go back and use the STAIRS or use the fabric to JUMP? ")
        print("\n")

AddToBag ('FABRIC')
AddToBag ('TORCH')
AddToBag ('BOTTLE')

"""START"""
#working
print("\n")
print("'Wha-where am I?' You push yourself to a sit as you're slowly gaining consciousness.")
print("The dim twilight barely reveals the ruins of an old castle tower around you.")
print("As you stand up to dust yourself off, you notice an unfamiliar satchel at your hip.")
print("You open it as your gaze follows your hand and inside it, you see:")
print("a small corked BOTTLE, a large peice of FABRIC and a TORCH.")
print("\n")
use = input("Which item do you pull out? ")

#working
if use.upper() == "FABRIC":
    print("\n")
    print("You unfold the large piece of fabric. As you’re examining it, the wind catches it and nearly blows it out of your hand.")
    print("Quickly catching the other end of the remnant, you watch the wind fill it up and get an idea!")
    print('\n')    
    use = input("Do you use the fabric to JUMP off the tower or WRAP around your shoulders for warmth? ")
#!!Broken!!
    if use.upper() == "JUMP":
        print("The castle grounds are slowly getting closer.  As you glide above them you can’t help but notice the gardens have obviously seen better days, but are still beautiful.  You’re in awe of the lush gardens until, suddenly, you hit the ground.  As you spit out the mouthful of grass, you get the eerie feeling someone is watching you. ")
#working
    elif use.upper() == "WRAP":
        print("\n")
        print("Wow! This fabric is a lot thicker and more sturdy than it originally felt.  You look fabulous and feel nice and toasty. ")
    else: next
    use = input("Do you want to JUMP off the tower, WRAP the fabric around your shoulders or look in your BAG for a different item? ")
    if use.upper() == "BAG":
        print("Your bag has:")
        print(bag)
        use = input("Which one to you take out? ")
if use.upper() == "BOTTLE":
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
#    print("You s.l.o.w.l.y and carefully start down the stairs.")
#    print("Amazingly, you reach the bottom safely!") 
#    print("Standing in what seems to be an old apothecary lab, you put your torch in a sconce nearby")
#    print("\n")
#    print("The oddly shaped jars catch your eye.")
#    print("Scanning the shelf, you see a jars labeled Squid TOES, powdered WATER and baking SODA.")
#    print("Not wanting to weigh down your satchel, you only want to take one bottle.")
#take = input("Which do you take? ")
#if take.upper() == "TOES":
#    AddToBag ("SQUID_TOES")
#if take.upper() == "WATER":
#    AddToBag ("POWDERED_WATER")
#if take.upper() == ("SODA"):
#    AddToBag ("BAKING_SODA")
   
#"""ROOM : TOWER"""
#if move.upper == "TOWER":
#    print("You walk down the narrow, cold stone pathway and enter the other tower.")
#    print("By the bright light of the torch, you can see a scorched portrait on the tower wall.")
#    print("Princess Etherea Chimericus: Keeper of the Dreams") 
#    print("you can barely make out the faint engraving")
#    print("on the small gold plaque under the large frame. ")
#    print("\n")
#    print("'Keeper of Dreams?' you wonder and your focus drops to the ground.")
#    print("On the ruin ground, just in front of your foot, your eyes catch the glint")
#take = input("of a gold coin. TAKE the coin or LEAVE it there?")
#if take.upper() == "TAKE":
#    AddToBag ("GOLD_COIN")
#else:
#    print("\n")
#    print("Suddenly, you remember how to breeze caught that fabric in your bag.")
#    use = input ("Do you go back and use the STAIRS or use the fabric to JUMP? ")
#    print("\n")
print ("Inventory: ")
print (bag)
print("END OF FINISHED CODE!")
print("\n")
#take = input('you wake up, type YES to add bottle to bag: ')
#if take.upper() == "YES":
#    AddToBag ('BOTTLE')
#else:
#    print('You leave the bottle there.')
#CheckInventory

#take = input('walk around, see a sword, type YES to pick it up: ')
#if take.upper() == "YES":
 #   AddToBag ('SWORD')
#else:
#    print('You leave the bottle there.')
#print (f'you now have:')
#print (bag)

#"""to delete from list"""


#give = input('guy wants your TORCH. type YES to give it to him ')
#if give.upper() == 'YES':
#    RemoveFromBag ('TORCH')
# else:
#   print('conequence')
#print ('you now have:')
#print (bag)
