#3 rooms window
from character import *
from rooms2 import *
from rooms import *


def room5a(character, canvas):
    stats(canvas)
    if canvas.data.visited5a == False:
        print "The tunnel goes on for some time, but eventually  you come out \
into a room with a large fountain. The room has one window. There are stairs \
to the east that go upward, and stairs to the south that go down."
        print "The water is clear and blue. The air in the room is fresh and \
clean. You breathe deep, and feel refreshed."
        canvas.data.XP += 1
        canvas.data.hp += 1
    else:
        print "You still find the fountain and the room refreshes you."
        canvas.data.hp += 1
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "examine":
            print "You look closely at the fountain \
it has dancing women and men, \
celebrating life, and drinking water from the fountain."
            action = raw_input("Do you want to take a drink? (yes or no)")
            if action == "yes":
                print "The water is cool and delicious."
                if canvas.data.hp <= 15:
                    canvas.data.hp += 5
                else:
                    canvas.data.hp += 2
            else:
                print "It's probably better that you didn't drink from a \
strange and mysterious water fountain, right?"
        elif (direction == "use water") or (direction == "use fountain"):
            print "You take a drink from the fountain and feel refreshed. \
The water is cool and delicious."
            if canvas.data.hp <= 15:
                canvas.data.hp += 5
            else:
                canvas.data.hp += 2
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. You eat the apple, \
and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "You light the torch, but the room is so bright, it \
doesn't really seem like a good decision. You immediately put it out"
                canvas.data.torchInUse = False
            else:
                print "You don't have a torch!"
        elif direction == "go east":
            canvas.data.visited5a = True
            check += 1
            print "'This looks like a lot of stairs,' you think."
            room6a(character, canvas)
        elif (direction == "go west"):
            canvas.data.visited5a = True
            check += 1
            room4a(character, canvas)
        elif direction == "go north":
            print "You don't want to throw yourself out the window. That \
is a bad idea. When you look out, you see the mountains that surround \
the one you're in. 'Where is the dragon?' You think."
        elif (direction == "go south"):
            canvas.data.visited5a = True
            print "Going down is much easier than going up."
            check += 1
            room5b(character, canvas)
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
        
def room5b(character, canvas):
    stats(canvas)
    if canvas.data.visited5b == False:
        print "The stairs wind down in a spiral. You start out, almost \
running down them, but after a while, you end up trudging. Finally, you \
come out into a great hall. You are amazed that a room like this exists \
under the mountain. You wonder who built this place, certainly, \
they are no longer around. You have yet to encounter homes, bed chambers, \
or kitchens. In fact, from what you've seen, it doesn't seem like people \
lived here."
        print "There are long tables that may have once been laden with \
food. There is a dias at the eastern end of the room. The throne is lying \
on its side. The silver is tarnished, the wood is crumbling, and the \
cushions are moldy. There is a door to the north and the south."
    else:
        "You wonder if the old hall is full of ghosts."
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "examine":
            print "You walk up to the throne and examine the intricate \
silver inlays. Dragons frolic along the surface. You pry a silver, fire \
breathing dragon from the wood. It is exquisitely carved with delicate \
features."
            if isInInventory("dragon", canvas) == False:
                print "You take the dragon."
                canvas.data.inventoryList += [["dragon"]]
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.XP += 2
            else:
                print "You've already picked up the dragon!"
                
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. You eat the apple, \
and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "You light the torch, but the room is so large, \
the torch can barely light a part of it. There is some sort of natural \
light in the room that you can't identify. You decide to put it out"
                canvas.data.torchInUse = False
            else:
                print "You don't have a torch!"
        elif direction == "go south":
            canvas.data.visited5b = True
            check += 1
            room5d(character, canvas)
        elif (direction == "go west"):
            canvas.data.visited5b = True
            check += 1
            room4b(character, canvas)
        elif direction == "go north":
            canvas.data.visited5b = True
            check += 1
            room5a(character, canvas)
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")
    
def scare(character, canvas):
    if character == "paladin":
        print "You can barely extend your arms all the way out in the little \
room, and suddenly, the walls begin to close in. They move slowly, but you \
can feel the panic rising inside you. You look up and see the ceiling coming \
toward you. The mage is laughing. 'There's no way to escape, ser. You are \
never going to slay the dragon, or get the princess. You will never be a \
lord. Her death will never be avenged.'"
        print "You are pushing at the walls and the ceiling. You are \
shouting, even though you know that no one is out there to save you. Visions \
of Lyane are dancing through your head, even as the walls press your arms to \
your sides. Your throat is starting to burn with all the screaming."
        saved = d20()
        if saved >=4:
            print "You are being crushed to death but suddenly the pressure \
is not that bad. Suddenly you can breathe again. The walls receede and two \
doors slide open, one to the north and one to the east. Through the eastern \
door you see a gigantic eye."
            canvas.data.XP +=10
            return
        else:
            print "You draw your sword and try to keep the walls apart \
but it snaps. Pieces of the broken sword embedded themselves into your \
skin. Unfortunately fate is cruel.\
The dice were rolled, and you came up without a chance."
            gameOver(character, canvas)
    else:
        print "Your feet are wet, and you look down to see the room is \
filling with water. Your heart begins to race. 'Why does it have to be \
water?' You shout at whatever gods might be listening."
        print "'Because that's what you dream of,' a voice says. At night \
when you are alone. You are afraid to close your eyes - afraid to sleep. \
Every night, when you finally drift off, you drown. You are swallowed by \
the ocean.'"
        print "You wonder if you can make a hole, and then drain the \
water out. You bang on the wall with your dagger; the water continues \
to rise around you. You chip stones, you dent some, but you can't make \
a big enough hole."
        print "The water rises up around your neck and you begin to scream. \
You shout and shout for help. Your mouth starts to fill with water as you \
use your last few breaths to try and get help."
        saved = d20()
        if saved >= 4:
            print "And suddenly, in a rush of water and stone, a doorway is \
opened to the east, and a large eye stares at you."
            canvas.data.XP +=10
            return
        else:
            print "You try and try to crack enough stones to get free but \
the water rushes in around you, down your throat, and into your lungs. You \
choke on the water and this time, there's no one to save you."
            gameOver(character, canvas)
            
def room5d(character, canvas):
    stats(canvas)
    #It's that mage again!!!
    if canvas.data.visited5d == False:
        print "You leave the great hall and enter a small room with no doors \
and no windows. You turn to leave, and realize the door you came in through \
is also gone. You are trapped."
    else:
        print "This is more of a passageway now."
    check = 0
    noEscape = True
    direction = raw_input("What do you want to do?")
    while check == 0:
        if noEscape == True:
            if (direction == "examine") or (direction == "listen"):
                print "You run your fingers along the wall where the door \
was. You cannot feel anything out of the ordinary. \
One of the stones seems to be loose."
                action = raw_input("Do you want to push on it? \
Or pull on it? (push or pull)?")
                if action == "pull":
                    print "You hear the mage's voice. He laughs, 'answer this \
riddle, and I'll let you go, slay the dragon, and claim your prize! The \
riddle is this: 'I never was, am always to be. No one ever saw me, nor \
ever will. And yet, I am the confidence of all, to live and breathe on this \
terrestrial ball.'"
                    answer = raw_input("What am I?")
                    if answer == "tomorrow":
                        print "'Correct,' he cackles, but no escape is \
opened for you."
                        scare(character, canvas)
                        noEscape = False
                    elif answer == "Tomorrow":
                        print "'Correct,' he cackles, but no escape is \
opened for you."
                        scare(character, canvas)
                        noEscape = False
                    else:
                        print "No, you lose, you fool. Tomorrow is the \
answer and it's something you will never live to see. The room begins to \
fill with water. You drown."
                        noEscape = False
                        check +=1
                        gameOver(character, canvas)
                elif action == "push":
                    scare(character, canvas)
                    noEscape = False
                else:
                    print "That's not an option right now!"
            else:
                print "That is not an option right now."
            direction = ("What do you want to do?")
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. You eat the apple, \
and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "You light the torch, but the room is so large, \
the torch can barely light a part of it. There is some sort of natural \
light in the room that you can't identify. You decide to put it out"
                canvas.data.torchInUse = False
            else:
                print "You don't have a torch!"
        elif (direction == "go east"):
            canvas.data.visited5b = True
            check += 1
            room6d(character, canvas)
        elif direction == "go north":
            canvas.data.visited5b = True
            check += 1
            room5b(character, canvas)
        else:
            unavailableOptions(direction)
        if gameOver == True:
            pass
        else:
            direction = raw_input("What do you want to do?")
                             
def room6a(character, canvas):
    stats(canvas)
    if canvas.data.visited6a == False:
        print "After climbing the steep stairs upward, you come out onto a \
stone balcony. You are at the top of the mountain. You can see, to your \
left, a large tunnel. A large plume of smoke, with flames on its heels, \
rises out of it. 'It has to be the dragon,' you think."
        print "You look out at the mountains. You could always turn back. \
You could turn away from this, probably, daft quest and seek safety. After \
a moment of doubt, of staring out at the sky, you decide to continue."
    else:
        print "The sky and the mountains are breathtaking, but you're \
wasting time."
    check = 0
    direction = raw_input("What do you want to do?")
    while check == 0:
        if direction == "examine":
            print "You can see that the large tunnel must be how the dragon \
travels from the bowels of the mountain to the sky. It is smooth, and and \
encrusted with small, what looks to be, diamonds. Whoever used to live in \
the mountain, they seemed to worship the dragon. Or maybe it was their \
prisoner."
        elif direction == "use apple":
            if isInInventory("apple", canvas) == True:
                print "You take the apple out of your bag and bite down. \
It is still sweet and a bit of juice runs down your chin. You eat the apple, \
and feel a bit better."
                canvas.data.inventoryList.remove(["apple"])
                print "Your inventory contains", canvas.data.inventoryList
                canvas.data.hp += 1
        elif direction == "use torch":
            if isInInventory("torch", canvas) == True:
                print "There's no reason to light a torch out here. \
You decide to put it out."
                canvas.data.torchInUse = False
            else:
                print "You don't have a torch!"
        elif (direction == "go west"):
            canvas.data.visited5b = True
            check += 1
            room5a(character, canvas)
        else:
            unavailableOptions(direction)
        direction = raw_input("What do you want to do?")

def room6d(character, canvas):
    stats(canvas)
    print "You enter a large cavern and in the center of it is a large \
red dragon with gold, spinning eyes, and black accent scales. It looks at \
you with less interest than you have for a fly or a worm. It huffs and in \
your mind you hear. 'Tiny human, you make too much noise.' You figure that \
the best thing you can do is look apologetic. After all, this magnificent \
queen just saved your life. \
You look around the room and see just the dragon, and some \
old, human bones."
    if character == "paladin":
        print "You don't see a princess. You search and search, and \
then you begin to wonder if the dragon ate her. If there was no princess \
to rescue, then there would be no lordship. You came to slay a dragon, and \
now, you've been saved by one."
        print "'Where is the princess?' You demand. 'I came by royal decree \
to rescue a princess!'The dragon rolls her eye at you and says, 'I sent \
that message out into the world. A rumor whispered here and there until \
someone made decree or a proclamation. You humans are so predictable. '"
        print "'Why did you need someone to come?' You ask. 'I needed a \
human, someone small to get at a nasty pest who has been bugging me, but \
who won't get close enough for me to deal with myself. There is a mage \
in this mountain who has destroyed my city and my worshipers. You will \
kill him for me."
    else:
        print "You don't see any gold, no gems, no jewels, no \
treasure, and the dragon saved your life. You came to slay it, and instead \
it turns out there is nothing to slay it for."
        print "Your mind reels as the dragon laughs inside your head. 'A \
puny-mortal, human like you thought it could slay me? That is a charmingly \
naieve idea indeed.' She blows a puff of hot air from her nose, it smells \
thick and lizardy. You grimace as you stumble to hold your balance."
        print "She moves her eye so that you are staring directly into it. \
'If there is someone that you would like to slay, I can charge you with a \
quest. Slay the mage that infests this place. He's driven away all my lovely \
human worshipers. He's a nuisance. Get rid of him for me. It will be an honor \
for you. I may even reward you."
    action = raw_input("Are you going to fight the mage?(yes or no)")
    if action == "yes":
        runMageBattle(character, canvas)
    else:
        print "'Very well,' the dragon says, turning away from you. You \
leave the wailing mountain with no glory and no dead dragon."
        gameOver(character,canvas)

def runMageBattle(character, canvas):
    print "You accept the dragon's offer and begin to hunt for the mage in \
the rest of the city which is accessed through the Dragon Room. You check \
through homes, and abandoned stores, and animal pens in need of repair."
    print "You camp at night in a small home, carved into the mountain. \
The furniture was still stable, and the straw-stuffed mattress was the \
least moldy. You fall asleep listening to the sound of the dragon \
moving about somewhere above you. Her presence permeates the city under her \
chamber."
    print "You come to a fork in the road. Both seem like decent options, \
but you're going to have to pick a direction."
    action = raw_input("Would you like to go left or right?")
    if action == "left":
        print "You turn down the left corridor. You find yourself in a \
circular chamber. In the center of the chamber are two statues. \
Both of the statues are in the shape of women, with bared flesh. They \
come to life with a hiss. They advance on you."
        move1 = ("Do you want to attack them? (yes or no)")
        if move1 == "no":
            print "They kill you."
            gameOver(character, canvas)
        else:
            statue1(canvas)
            print "You attack the first one! The second one hangs back from \
her sister, glaring at you with black eyes."
            attack(canvas.data.hp,
                   canvas.data.dp,
                   canvas.data.monster,
                   canvas.data.monsterHP,
                   canvas.data.monsterDP, canvas)
            print "The second one comes at you with a scream."
            statue2(canvas)
            attack(canvas.data.hp,
                   canvas.data.dp,
                   canvas.data.monster,
                   canvas.data.monsterHP,
                   canvas.data.monsterDP, canvas)
            print "Now that you've killed them both. And there is no where \
else to go from this room except back, you go back the way you came so that \
you can take the right corridor."
            mageBattle(character, canvas)
    else:
        print "You turn down the right corridor and he is standing in your \
path."
        mageBattle(character, canvas)
    print "The dragon trumpets when she sees you carrying the mage. She \
tells you to lay him down and then she blows a great blaze of blue fire \
onto his body. He catches immediately, and you both watch him burn."
    endOfGame(character, canvas)

def mageBattle(character, canvas):
    stats(canvas)
    print "He laughs. His hands are drenched in blood. You can see a dead \
animal carcass behind him. 'I've been expecting you.'"
    print "You see him now, not just as a mage, but as a man. He is old, \
older than anyone should rightfully be. His hands are almost skeletal. \
He is gaunt and his teeth are rotten and yellow. His eye sockets are \
sunken and his skin is sallow. If he were not a mage, he would just be a \
weak old man."
    action = raw_input("Do you attack? (yes or no)")
    if action == "no":
        print "You don't attack him, he's just a frail old man, after all. \
Compassion is a good thing, but he has none and before you can tell him that \
you're leaving him to his own misery, he boils the blood in your veins and \
you die screaming."
        gameOver(character, canvas)
    else:
        print "You rush forward and strike at him, but he is gone in a flash \
of light. He reappears behind you and strikes you."
        print "He does", d6(), "damage to you. Then he disappears again, \
laughing wildly. When he reappears, you strike at him again with your fist, \
and this time, you get him with. You do",d6(),"damage to him."
        mage(canvas)
        action2 = raw_input("You have two choices. You could keep swinging at \
him or you could try to trick him. What do you do? (swing or trick)")
        if action2 == "swing":
            attack(canvas.data.hp,
                   canvas.data.dp,
                   canvas.data.monster,
                   canvas.data.monsterHP,
                   canvas.data.monsterDP, canvas)
            print "You scoop up his defeated body and carry it back to the \
dragon."
        else:
            print "You pretend to give up. You pretend to cower, briefly. \
and he starts chanting. You try to put fear in your eyes. You offer him \
anything he could desire. You offer him everything you have. He laughs. He \
thinks that he's won."
            print "He sweetly offers you a hand, saying he is glad for you \
because you realized he couldn't be beat. You grab his hand and then, firmly \
pull him forward onto your", canvas.data.weapon,". His eyes go wide as it \
guts him, and you let him fall to the floor."
            print "You carry his body back to the dragon."
            
                                         
def endOfGame(character, canvas):
    stats(canvas)
    print "True to her word, the dragon rewarded you by carrying you out of \
the Wailing Mountain in one taloned claw. In the other, she carried a fortune \
that you wrapped up in a large canvas that was in one of the abandoned \
houses. The gold was hidden away in a vast pit that the dragon settled over \
to sleep."
    if character == "paladin":
        print "She takes you to your lord father's manse, and without a word \
she leaves you there. The whole household emptied itself into the courtyard \
to watch your arrival. Your father, it turns out, died just that morning. \
You are now lord of Alten Roa. You take your place there and build a garden \
for Lyane, full of golden flowers."
    else:
        print "She takes you to the home you grew up in, which has been \
neglected since you left as a young man of 15. You drag in the gold, and \
then you begin clearing the cobwebs and mending the eves. You look forward \
to building a new house on this spot where you can quietly go into \
retirement. In the front yard, you'll build a garden full of sweet smelling \
flowers for your mother."
    gameOver(character, canvas)

def gameOver(character, canvas):
    print "             \
[[[GAME OVER]]]"
    canvas.data.gameOver == True
