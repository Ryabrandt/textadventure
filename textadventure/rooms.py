#Rooms
from character import *
from rooms2 import *
from rooms3 import *

def cmmdList():
    print "{-----COMMAND LIST-----}"
    print "go (north, south, east, west)"
    print "take (item)"
    print "use (item)"
    print "attack"
    print "listen"
    print "examine"
    print "stats - to give you a list of your stats and inventory"
    print "commands - to get a list this list of commands again."
    print "{-----END COMMAND LIST-----}"
    return

def openingScreen(canvas):
    print "Welcome! This game is called 'Here There Be Dragons... Oh, and \
over there too'."
    print "Before we get started, this is the list of commands that \
you can use when prompted. All commands are lower case. \
If you want to call up the list again, just type \
the word 'commands' when asked 'What do you want to do?'"
    cmmdList()
    play = raw_input("Do you want to play \
'Here there Be Dragons... Oh, and over there too'? (yes or no.)")
    if play == "yes":
        startGame(canvas)
    else:
        pass


def startGame(canvas):
    createCharacter(canvas)
    if canvas.data.character == "paladin":
        preRoomPaladin(canvas)
    elif canvas.data.character == "rogue":
        preRoomRogue(canvas)
    else:
        canvas.data.character == "rogue"
        preRoomRogue(canvas)

        
#PreRooms - this is where pre-gameplay is stored
def preRoomPaladin(canvas):
    stats(canvas)
    canvas.data.location = "preRoomPaladin"
    print "You are",canvas.data.name,", a white knight of the\
 order of The Lion. You have spent ten years training and studying, praying,\
 and waiting for the day that the Lord of Light would send you out\
 in his name. You are ready to vanquish evil, and bring justice to the people.\
 You are travelling eastward across the vast plains when you hear from a passing\
 troupe that the Princess of the Third Kingdom has been abducted by the dragon,\
 Dark Scale. You reach the village of Kettan as the sun is setting behind the\
 Wailing Mountain. You enter a smokey inn, full of men and women whispering in\
 their cups. There is a bar on the north side of the room and a table where\
 you can sit alone on the opposite side."
    #Start of options
    direction = raw_input("What do you want to do?")
    if direction == "go north":
        print "The barman is wiping a glass with a questionable looking rag.\
 He does not smile at you. He sets down the glass and fills it with a red\
 ale and grunts, 'two gold'."
        direction = raw_input("Do you want to pay him? (yes or no)")
        if direction == "yes":
            canvas.data.gold -= 2
            
        else:
            print "'Fine, no beer for you!' he huffs angrily."

    elif direction == "go south":
        print "You sit at a quiet table by yourself and watch the room."
    elif direction == "use apple":
        if isInInventory("apple", canvas) == True:
            print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
            canvas.data.inventoryList.remove(["apple"])
            print "Your inventory contains", canvas.data.inventoryList
            canvas.data.hp += 1
        else:
            print "You don't have an apple to use."    
    else:
        unavailableOptions(direction)
    print "A man in a glorified potato sack comes up to you with a crumpled \
piece of parchment. 'Read this,' he mutters. You \
unwrap it and reveal a royal decree. It says that the princess has been \
kidnapped by the dragon in the Wailing Mountains. The King is offering a \
lordship to the knight who can rescue the princess."
    play = raw_input("Are you going to rescue the princess?")
    if play == "yes":
        canvas.data.XP +=1
        print "You just earned 1 XP!"
        room1a("paladin",canvas)
    elif play == "no":
        openingScreen(canvas)
            
def preRoomRogue(canvas):
    stats(canvas)
    canvas.data.location = "preRoomRogue"
    print " You are",canvas.data.name,", and in some circles, you're \
famous for your sticky fingers. You have just finished a job stealing \
the jewels from a duchess' dress. You snatched them right off of the hem \
without her discovering you. Her husband, the Duke, however, caught you \
stuffing your pockets with them. You find yourself in a small town tavern \
in the villiage of Kettan. There are a few people playing dice at one table. \
The bar keep is wiping down the bar with a dirty rag."
    direction = raw_input("What do you want to do?")
    if direction == "go north":
        print " The barman barely looks up at you. He glances but \
he does not smile at you or greet you. \
He sets down the glass and fills it with a red\
ale and grunts, 'two gold'."
        direction = raw_input("Do you want to pay him? (yes or no)")
        if direction == "yes":
            canvas.data.gold -= 2
            print "There's a hair in your beer. The barkeep is bald. \
You dump the rest of the brown liquid on the floor."
        
        else:
            print " 'Fine, no beer for you!' he huffs angrily."

    elif direction == "go south":
        print " You sit at a quiet table by yourself and watch the room."
    elif direction == "use apple":
        if isInInventory("apple", canvas) == True:
            print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
            canvas.data.inventoryList.remove(["apple"])
            print "Your inventory contains", canvas.data.inventoryList
            canvas.data.hp += 1
        else:
            print "You don't have an apple to use."        
    else:
        unavailableOptions(direction)
    print " You sit, listening to the crowd. It's been a long road, \
and you are tired. You're starting \
to dream about settling into a large manse, with servants, and food, and a \
warm bed every night. You chuckle, thinking about people picking your pockets \
and trying to con you."
    print " A couple of dirty men are drinking and muttering. \
You lean in and hear, the man with the muddy hair say, \
'There's a lot of gold under the mountain.' The other one, the greasy one, \
smacks his lips and grimaces. 'Ain't no way to get at it with that dragon \
sitting on it like a lord.' The first one nods, grimly. You aren't afraid \
of one dragon, right?"
    play = raw_input("Are you going after the gold? (yes or no)")
    if play == "yes":
        canvas.data.XP += 1
        print "You just gained 1XP."
        room1a("rogue",canvas)
    elif play == "no":
        print "----------------------------------"
        openingScreen(canvas)

def room1a(character, canvas):
    stats(canvas)
    check = 0
    if canvas.data.visited1a ==  False:
        print canvas.data.name, ", you travelled for three days to \
the Wailing Mountain and enter through a cave at \
the base of the mountain. The chamber is lit with light from outside.\
There is a door to the east and a door to the south. An unlit torch and \
a single \
skull is laying on the floor, its vacant eye holes are staring \
up at you."
        direction = raw_input("What do you want to do?")
    else:
        print "There's nothing new here. The doors are to the south \
and the east."
        direction = raw_input("What do you want to do?")
    while check == 0:
        #items in this room: torch, skull
        if direction == "go south":
            canvas.data.visited1a = True
            check +=1
            room1b(character, canvas)
        elif direction == "go east":
            check+=1
            canvas.data.visited1a = True
            room2a(character, canvas)
        elif direction == "take skull":
            if isInInventory("skull", canvas) == False:
                print "You picked up the skull."
                canvas.data.inventoryList += [["skull"]]
                print "Your inventory contains", canvas.data.inventoryList
            else:
                print "You've already picked that up!"
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
            else:
                print "You don't have an apple to use."
        elif direction == "take torch":
            if isInInventory("torch",canvas) == False:
                canvas.data.inventoryList += [["torch"]]
                print "You picked up the torch."
                print "Your inventory contains", canvas.data.inventoryList
            else:
                print "You've already picked that up!"
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")

def room1b(character,canvas):
    stats(canvas)
    canvas.data.monsterLives = 1
    if canvas.data.visited1b == False:
        print"You are in a small chamber with no lights. \
The smell of rotten meat and an unrecognizable foul odor, \
mingle. The air is humid and you cough and turn to leave, \
only to discover that the way you came in is now blocked by \
by off by a stone door. \
It is the only exit. \
You hear a low growl coming from the darkness."
    else:
        print "There's nothing but that dead troll in this room. \
You go back north to the other room."
        room1a(character, canvas)
    check = 0
    riverTroll(canvas)
    direction = raw_input("What do you want to do?")
    while check == 0:
        while canvas.data.monsterLives == 1:
            if direction == "listen":
                roll = d20()
                if roll >=10:
                    print "You stand perfectly still and hold your breath, listening \
to the growling. It gets steadily louder as the thing in the darkness comes toward you."
                else:
                    "You just hear the low growl."
            elif direction == "use apple":
                if isInInventory("apple", canvas) == True:
                    print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
                    canvas.data.inventoryList.remove(["apple"])
                    print "Your inventory contains", canvas.data.inventoryList
                    canvas.data.hp += 1
                else:
                    print "You don't have an apple to use."                   
            elif direction =="attack":
                roll = d20()
                if roll >= 10:
                    print "You strike out at the noise with your", canvas.data.weapon,\
                          "and it strikes something that howls with surprise and rage. \
A large", canvas.data.monster, " wanders toward you. You can make out the moss \
green of its large round eyes."
                    attack(canvas.data.hp, canvas.data.dp,
                                       canvas.data.monster, canvas.data.monsterHP,
                                       canvas.data.monsterDP, canvas)
                else:
                    "You're not attacking anything!"
            elif direction == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "The torch illuminates the room \
and you see a river troll!"
                else:
                    print "You can't use what you don't have."
            else:
                unavailableOptions(direction)
                direction = raw_input("What do you want to do?")
            direction = raw_input("What do you want to do?")
        if direction == "go north":
            check += 1
            canvas.data.visited1b = True
            room1a(character,canvas)
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "The torch illuminates the room, you see the dead troll."
                canvas.data.torchInUse = True
            else:
                print "You don't have a torch!"
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
            else:
                print "You don't have an apple to use."
        elif direction == "listen":
            print "You don't hear anything but the sound of your own heart."
        else:
            unavailableOptions(direction)
            direction = raw_input("What do you want to do?")
    direction = raw_input("What do you want to do?")

def room2a(character,canvas):
    #items in this room: rags cover a diamond,
    #a dagger, a health draught worth +1 hp
    stats(canvas)
    check = 0
    while canvas.data.visited2a == False:
        print "The room seems to eminate a blue light from the walls. \
You can go south or back the way you came \
There is some writing on the north wall. You can go south or west.\
The room is cold, it chills you all the way to the core."
        if character == "paladin":
            print "*You remember yourself, as a boy, falling into an abandoned \
well. You weren't supposed to go off on your own, but you snuck away from \
training. You were fighting imaginary ghosts with a large stick when the \
ground gave way from beneath you. It seemed like hours that you laid in the \
freezing water. Your lips turned blue, and you lost the feeling in your \
hands and feet. They found you the next morning, almost frozen from the cold. \
Your fingers and toes were bloody from trying to scramble up the walls of the \
well.* The memory lingers in your mind in this room."
            canvas.data.XP += 5
        if character == "rogue":
            print "You aren't bothered by a little bit of cold, but the eerie \
glow from the walls reminds you of almost drowning in the Cerulean Sea last \
sumemr. You were taking a ship from Callos to Lys during a storm. You paid \
extra for the haste, because the King of Callos, his royal, fat-cherub \
was offering a hundred gold pieces for your head. During the storm, you \
were tipped from the deck. Your head bounced, soundly off the side of the \
and you landed in the water, dazed. The blue ocean pressed in around you \
filling your lungs until you drowned. You woke up on the deck of the ship \
to one of the sailors, pushing air into your lungs, and forcing your heart \
to beat."
            canvas.data.XP += 5
        direction = raw_input("What do you want to do?")
        while check == 0:
            if direction == "go south":
                canvas.data.visited2a = True
                room2b(character,canvas)
                check += 1
            elif direction == "go west":
                canvas.data.visited2a = True
                room1a(character,canvas)
                check += 1
            elif direction == "examine":
                print "There is writing on the wall, in what appears to be fresh \
blood. It says, 'Beware! The dragon is not the worst fate ahead. Turn back!' \
You are not afraid. You are a brave, bold adventurer. Whatever is ahead, you \
can deal with it."
            elif direction == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "The torch does not help to stave off the cold or the \
strange glow from the walls."
                    canvas.data.torchInUse = True
                else:
                    print "You don't have a torch!"
            elif direction == "use apple":
                if isInInventory("apple", canvas) == True:
                    print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
                    canvas.data.inventoryList.remove(["apple"])
                    print "Your inventory contains", canvas.data.inventoryList
                    canvas.data.hp += 1
                else:
                    print "You don't have an apple to use."
            else:
                unavailableOptions(direction)
            direction = raw_input("What do you want to do?")
    print "The writing on the wall is oozing a shiny trail down the walls, and \
puddling on the floor, running in the channels between the stone. You can go \
south or west"
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "go south":
            canvas.data.visited2a = True
            room2b(character,canvas)
            check += 1
        elif direction == "go west":
            canvas.data.visited2a = True
            room1a(character,canvas)
            check += 1
        elif direction == "examine":
            print "There is writing on the wall, in what appears to be fresh \
blood. It says, 'Beware! The dragon is not the worst fate ahead. Turn back!' \
You are not afraid. You are a brave, bold adventurer. Whatever is ahead, you \
can deal with it."
            canvas.data.XP +=1
            print "You've gained 1 XP!"
        elif direction == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "The torch does not help to stave off the cold or the \
strange glow from the walls."
                    canvas.data.torchInUse = True
                else:
                    print "You don't have a torch!"
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
            else:
                print "You don't have an apple to use."
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
    
def room2b(character,canvas):
    #suit of armor room
    #Items -> torches
    stats(canvas)
    check  = 0
    canvas.data.monsterLives = 1
    while canvas.data.visited2b == False:
        print "The room is lit with torches. There are no doors. You begin \
to turn around, ready to leave, when you hear a creak. You turn back."
        print "There is a suit of armor, standing in an archway that you \
could swear wasn't there before. It is carrying a longsword. There are \
brown stains spattered over the chest and hands. 'Blood,' you think."
        print "You walk toward it."
        suitOfArmor(canvas)
        direction = raw_input("What do you want to do?")
        while check == 0:
            while canvas.data.monsterLives == 1:
                if direction == "examine":
                    print "The armor is old. The style looks like ancient \
Calloran. You recognize it from the museums of Arden and the art of Talek. \
No one in the world builds armor like this any more. As you study it, the \
armor seems to twitch. It creaks wide and you jump when it begins to speak."
                    riddleArmor(canvas)
                    direction = "none"
                elif direction == "attack":
                    roll = d20()
                    if roll >= 2:
                        print "You push the suit of armor, expecting it \
to fall over. It rocks once and then springs to life, slashing at you with \
the longsword. It nicks your arm, and you jump back."
                        attack(canvas.data.hp,
                               canvas.data.dp,
                               canvas.data.monster,
                               canvas.data.monsterHP,
                               canvas.data.monsterDP, canvas)
                        print "The defeated armor shudders and the room \
rumbles around you. A door to the East slides open. You cannot see into \
the darkness."
                        direction = raw_input("What do you want to do?")
                    else:
                        print "You missed pushing something that is \
standing still. Stop drinking and try again."
                elif direction == "flee":
                    print "You try to run, but you cannot escape. \
Before you can get out of the room, the armor comes to life and cuts \
you down."
                    check +=1
                    gameOver(character, canvas)
                elif direction == "take armor":
                    print "You can't take that!"
                else:
                    unavailableOptions(direction)
                direction = raw_input("What do you want to do?")
            if direction == "go east":
                canvas.data.visited2b = True
                check += 1
                room3b(character,canvas)
            elif direction == "take torch":
                if isInInventory("torch",canvas) == False:
                    canvas.data.inventoryList += [["torch"]]
                    print "You picked up the torch."
                    print "Your inventory contains", canvas.data.inventoryList
                else:
                    print "You've already got a torch!"
            elif direction == "use torch":
                if isInInventory("torch", canvas) == True:
                    print "The torch doesn't do much in this room."
                    canvas.data.torchInUse = True
                else:
                    print "You don't have a torch!"
            elif direction == "use apple":
                if isInInventory("apple", canvas) == True:
                    print "You take the apple out of your bag and bite down. It is \
still sweet and a bit of juice runs down your chin. You eat the apple, and \
feel a bit better."
                    canvas.data.inventoryList.remove(["apple"])
                    print "Your inventory contains", canvas.data.inventoryList
                    canvas.data.hp += 1
                else:
                    print "You don't have an apple to use."
                
            else:
                unavailableOptions(direction)
            direction = raw_input("What do you want to do?")
            
