#More rooms
from character import *
from rooms import *
from rooms3 import *

def riddleArmor(canvas):
    print canvas.data.name,"You will answer this riddle or you will not move \
on. The riddle: I end the 'race'. I am at the beginning of the 'end'. I am at \
the start of 'eternity' and the end of 'space'. There are two of me in \
'heaven' and one in 'hell'. I am in 'water', 'fire', 'sunshine', and \
'darkness'. I am the beginning of 'earth' and the end of 'life'."
    answer = raw_input("What am I?")
    answerCount = 3
    while answerCount > 0:
        if answer == "e":
            print "'You are correct!', it tells you. It steps aside opening \
the way for you."
            canvas.data.XP += 15
            canvas.data.monsterLives -= 1
            answerCount = -1
        elif answer == "E":
            print "You have passed the first test. Now you must fight me!"
            answerCount = -1
            canvas.data.XP += 5
            attack(canvas.data.hp,
                   canvas.data.dp,
                   canvas.data.monster,
                   canvas.data.monsterHP,
                   canvas.data.monsterDP, canvas)
            canvas.data.XP += 15
        elif answer == "attack":
            print "You try to attack the suit of armor. Nothing happens."
        elif answer == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "Using the torch doesn't do much in this room."
                    canvas.data.torchInUse = True
                else:
                    print "You don't have a torch!"
        elif (answer == "flee") or (answer == "go north"):
            print "You try to run, but it cuts you down!"
            answerCount = -1
            gameOver(character, canvas)
        else:
            print "You have", answerCount,"more chances to answer."
    if answerCount == 0:
        print "'You fool, you cannot answer a simple riddle?' It shouts. \
Without warning, it lifts it's sword and kills you."
        gameOver(character,canvas)
    return
        
def room3b(character, canvas):
    stats(canvas)
    #No Items
    #Big fricken tunnel!
    check = 0
    if canvas.data.visited3b == True:
        print "The hallway is still just an ominous dark hallway."
    while canvas.data.visited3b == False:
        if canvas.data.torchInUse == True:
            print "Your torch illuminates the hallway. It's made of a rough, \
gray stone. A silver vein runs through the stones, from one to the next. \
You walk, following it from one stone to the next, \
for what seems like a mile. You keep walking down into the darkness.\
You see an opening to the north. Or you could continue going east."
        else:
            print "You cannot see down the hallway. \
The stone is rough. You start walking, deeper into the darkness. \
The darkness closes in on you. It tightens its grip, and you start to run \
down the corridor, blindly trying to find your way to the other end. As you \
run, you drag your fingertips along the stone."
            print "Suddenly, you come to an opening in the stone to the north. \
The air in that direction is cooler, somewhat fresher. There are two ways you \
can go - north or east."
        direction = raw_input("What do you want to do?")
        if direction == "go east":
            canvas.data.visited3b = True
            check +=1
            room4b(character, canvas)
        elif direction == "go north":
            print "You turn up the hallway to the north, toward the cleaner, \
fresher air. You walk, upwards. The climb gets steeper and steeper."
            canvas.data.visited3b = True
            check += 1
            room3a(character, canvas)
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "Your torch illuminates the hallway. It's made of a \
rough, gray stone. \
A silver vein runs through the stones, from one to the next. \
You walk, following it from one stone to the next, \
for what seems like a mile. You keep walking down into the darkness.\
You see an opening to the north. Or you could continue on."
                canvas.data.torchInUse = True
            else:
                print "You don't have a torch!"
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. \
You eat the apple, and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "listen":
            print "You hear your own heart beat. The sound of rushing water \
is coming from... somewhere, but you can't quite tell where. You hear the \
a clicking noise, faint, but it is there and you can hear it when you listen \
closely."
        elif (direction == "examine") and (canvas.data.torchInUse == True):
            print "The silver in the walls appears to be laid in by hand, \
but made to look as if it was buried within the stone. It is covered in a \
fine layer of dust. As you brush the dust away, you feel sad and lonely. \
You think about your mother, and your family, and places far away that you \
haven't seen in a long time."
        else:
            unavailableOptions(direction)
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "go east":
            canvas.data.visited3b = True
            check +=1
            room4b(character, canvas)
        elif direction == "go north":
            print "You turn up the hallway to the north, toward the cleaner, \
fresher air. You walk, upwards. The climb gets steeper and steeper."
            canvas.data.visited3b = True
            check += 1
            room3a(character, canvas)
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "The torch allows you to see the stone walls around you."
        elif (direction == "examine") and (canvas.data.torchInUse == True):
            print "The silver in the walls appears to be laid in by hand, \
but made to look as if it was buried within the stone. It is covered in a \
fine layer of dust. As you brush the dust away, you feel sad and lonely. \
You think about your mother, and your family, and places far away that you \
haven't seen in a long time."
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")

def room3a(character, canvas):
    stats(canvas)
    #no items
    #mage - with lots of xp - BIG FIGHT
    canvas.data.monsterLives = 1
    check = 0
    if canvas.data.visited3a == False:
        print "You reach some stairs. They are steep and carved from the same \
stone as the walls. You climb and enter a room that looks like a dungeon. It \
is circular and lined with cells. There is a door to the east, and you can \
always go back the way you came."
        print "Most of the cells seem empty but there might be a few cells \
that are worth checking into."
    direction = raw_input("What do you want to do?")
    while canvas.data.monsterLives == 1:
        if direction == "examine":
            print "You examine the northern cell. It has a few rags in it \
and you paw through them. You move from cell to cell, inspecting them. After \
looking through three cells, you start to have the feeling of being watched. \
You turn around to see a woman, staring at you. She's crying."
            talk = raw_input("Do you want to talk to her? (yes or no)")
            if talk == "yes":
                print "You walk up to the cell she's in, and ask, 'Do you \
need my help?' She nods. You try to break open the cage but as you do so, a \
bright light fills the room. At first, you shield your eyes and she falls to \
the floor with a wail. Then, as the light dies away, you see him. He's \
standing behind her in the cell and his eyes are wild. He looks insane. 'A \
mage,' you think."
                print "He laughs, his contaminated, blood-red eyes spark \
wildly. He grabs the woman by the hair and suddenly, she's not a stranger."
                if character == "paladin":
                    print "It's Lyane. Her green eyes are full of tears. \
Her blonde hair is matted with blood. She's screaming as your father is \
dragging her into the courtyard. She's crying out for you to help her, to \
save her. You love her. You watched as he dragged her into the yard and \
killed her. You see it, happening, in front of you. It's happening again."
                    print "She's crying out and your father is drawing \
out his sword. He raises it up over his head and before you can stop him, \
her head is rolling across the grass. It lands at your feet and you look up \
at the mage, who is cackling at you, wildly, waving around an empty potato \
sack."
                    canvas.data.XP += 5
                elif character == "rogue":
                    print "It's your mother. Her blue eyes are wide, and \
she's panicking. The men holding her are smiling. The one holding you is \
laughing as you struggle. You're struggling against his large hands, when \
just that morning he was helping you pull up weeds in the garden. You \
thought he was going to be your father. Now he's holding your seven year \
old self while his associates tear apart your home, looking for things to \
steal, and raping your mother."
                    print "They killed her. In the end, he stabbed her, \
and then he stabbed you. He put his knife in you, and laughed. You bled. You \
bled on the floor until someone found you, staring into her dead eyes."
                    print "The mage is laughing, holding onto an empty \
sack. He shakes the sack and laughs."
                    canvas.data.XP += 5
            else:
                print "You turn away from her, and then you look back and \
nothing is there but an empty sack."
            direction = raw_input("What do you want to do?")
            if direction == "attack":
                print "You rush forward and grab the bars to attack \
the mage but he disappears in a flash."
                canvas.data.monsterLives -= 1
            elif direction == "flee":
                print "You can't run from the past."
            elif direction == "go south":
                print "You go back the way you came."
                canvas.data.visited3a = True
                room3b(character, canvas)
            elif direction == "go east":
                canvas.data.visited3a = True
                room4a(character, canvas)
            elif direction == "use apple":
                if isInInventory("apple", canvas) == True:
                    print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. \
You eat the apple, and feel a bit better."
                    canvas.data.inventoryList.remove(["apple"])
                    print "Your inventory contains", canvas.data.inventoryList
                    canvas.data.hp += 1
            elif direction == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "The torch doesn't do much in this room."
                    canvas.data.torchInUse = True
                else:
                    print "You don't have a torch!"
            else:
                unavailableOptions(direction)
            direction = raw_input("What do you want to do?")
        elif direction == "go south":
                print "You go back the way you came."
                canvas.data.visited3a = True
                room3b(character, canvas)
        elif direction == "go east":
            canvas.data.visited3a = True
            room4a(character, canvas)
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "go south":
                print "You go back the way you came."
                canvas.data.visited3a = True
                room3b(character, canvas)
        elif direction == "go east":
            canvas.data.visited3a = True
            room4a(character, canvas)
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
    direction = raw_input("What do you want to do?")
            
def room4a(character, canvas):
    stats(canvas)
    if canvas.data.visited4a == False:
        print "You start to wonder if you should turn back. \
You shudder. The short hallway opens into a vast \
chamber. At first, you have a hard time recognizing what you're looking at. \
Then, things seem to come into focus and you realize you're in some sort of \
torture chamber. An iron maiden stands in one corner, rusting. A rack, its \
chains coiled on the floor, appears to be falling apart. A cage in one corner \
has a forgotten skeleton lying in it."
    else:
        print "This torture chamber feels haunted."
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "examine":
                print "The iron maiden is covered in brown blood. A faint \
smell of rotting meat permeates the room. The rack is made of wood and it \
seems like termites have taken their toll. The bones in the cage are clean."
        elif direction == "listen":
            print "You can hear laughter in the distance, and a strange \
clicking noise."
        elif direction == "go west":
            print "You go back the way you came."
            canvas.data.visited4a = True
            check += 1
            room3a(character, canvas)
        elif direction == "go north":
            canvas.data.visited4a = True
            check+=1
            room4c(character, canvas)
        elif direction == "go south":
            canvas.data.visited4a = True
            check +=1
            room4b(character, canvas)
        elif direction == "go east":
            canvas.data.visited4a = True
            check += 1
            room5a(character, canvas)
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. \
You eat the apple, and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "The torch doesn't do much in this room but add an \
eerie orange glow to the dangerous items it contains."
                canvas.data.torchInUse = True
            else:
                print "You don't have a torch!"
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")

def room4c(character, canvas):
    stats(canvas)
    if canvas.data.visited4c == False:
        print "You are starting to feel tired. You have been walking for \
hours. Your eyes are heavy and your body feels week. The room you enter is \
warm. The floor is covered in straw. You let your bag fall to the floor. You \
start to doze. Your eyes close and fall asleep."
        print "You wake up some time later, the room is freezing. You see \
your breath coming out in long, smoky tendrils. You try to rise, and find \
your muscles stiff, and weak. You call out, but there is no answer."
        print "You drag yourself into a sitting position and suddenly,\
you remember."
        dream(character,canvas)
    else:
        print "The room no longer has the same effect on you."
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "examine":
            print "The room is circular, with a bare stone floor."
        elif direction == "listen":
            print "You can hear laughter in the distance, and a strange \
clicking noise."
        elif direction == "go south":
            print "You go back the way you came."
            canvas.data.visited4c = True
            check += 1
            room4a(character, canvas)
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. \
You eat the apple, and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "The torch doesn't do much in this room."
                canvas.data.torchInUse = True
            else:
                print "You don't have a torch!"
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
        
def room4b(character, canvas):
    stats(canvas)
    #Items - Diamond
    if canvas.data.visited4b == False:
        print "You follow a blue light until you find yourself standing at \
the bottom of a small ampitheatre. You can go north and south, or back the \
way you came. You step out on to the stage, and you can smell something like \
wet dog. You turn, slowly, and find a large warg, silently stalking you. Its \
gold eyes glimmer with hunger."
    else:
        print "This place is so strange, it really makes you feel sick."
    canvas.data.monsterLives = 1
    warg(canvas)
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        while canvas.data.monsterLives == 1:
            if direction == "attack":
                attack(canvas.data.hp,
                   canvas.data.dp,
                   canvas.data.monster,
                   canvas.data.monsterHP,
                   canvas.data.monsterDP, canvas)
                canvas.data.XP += 2
                print "The warg drops a diamond the size of your fist."
                action = raw_input("Do you want to pick it up? (yes or no)")
                if action == "yes":
                    if isInInventory("diamond", canvas) == False:
                        print "You pick it up and, far in the distance, \
you think you hear a scream."
                        canvas.data.inventoryList += [["diamond"]]
                        print "Your inventory \
contains",canvas.data.inventoryList
                    else:
                        print "You've already picked that up!"
                    
                else:
                    print "You decide it's better left alone."
            elif direction == "examine":
                print "The warg is a large, viscious dog-like beast. It's \
fur is coarse, and dark. It seems really angry. You should be careful."
            elif direction == "use apple":
                if isInInventory("apple", canvas) == True:
                    print "Why do you want to eat an apple while there's a \
giant warg in front of you? That seems like a waste of time!"
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
            elif direction == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "The warg doesn't seem to be afraid of the torch."
                    canvas.data.torchInUse = True
                else:
                    print "You don't have a torch!"
            elif direction == "go east":
                print "The warg is blocking your way."
            elif (direction == "go west") or (direction == "flee"):
                print "You try to run, but it grabs you and drags you back."
            elif direction == "go north":
                print "The warg is blocking your way."
            else:
                unavailableOptions(direction)
            direction = raw_input("What do you want to do?")
        if direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. You eat the apple, \
and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "You light the warg on fire and watch it burn. \
Kind of sick."
                canvas.data.torchInUse = True
            else:
                print "You don't have a torch!"
        elif direction == "examine":
            print "The eastern door is ringed in symbols. It is old Garuvan. \
The language is virtually dead. The mages guild still uses the symbols, not \
for writing, but for their power and connections to the old gods."
        elif direction == "go east":
            canvas.data.visited4b = True
            check += 1
            print "The eastern door is ringed in symbols"
            room5b(character, canvas)
        elif (direction == "go west"):
            canvas.data.visited4b = True
            check += 1
            room3b(character, canvas)
        elif direction == "go north":
            canvas.data.visited4b = True
            check += 1
            room4a(character, canvas)
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
