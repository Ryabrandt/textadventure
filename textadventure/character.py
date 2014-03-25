#Characters
#D20, Mage, Attack, warg, troll
import random

def d20():
    return random.randint(1,20)

def d6():
    return random.randint(1,6)
def dWithZero():
    return random.randint(0,6)

def rollHP(charType):
    if charType == "rogue":
        HP = random.randint(10,20)
        return HP
    elif charType == "paladin":
        HP = random.randint(15,30)
        return HP

def rollDP(charType):
    if charType == "rogue":
        DP = random.randint(15,30)
    elif charType == "paladin":
        DP = random.randint(10,20)
    return DP

def getStartingGold(canvas):
    goldLoop = random.randint(1,10)
    gold = 0
    for g in range(goldLoop):
        gold += random.randint(1,1000)
    return gold


def unavailableOptions(direction):
    if direction == "go east":
        print "You can't go that way!"
    elif direction == "go west":
        print "You can't go that way!"
    elif direction == "go north":
        print "You can't go that way!"
    elif direction == "go south":
        print "You can't go that way!"
    elif direction == "take":
        print "There is nothing to take."
    elif direction == "attack":
        print "You look crazy, there's nothing for you to attack."
    elif direction == "use":
        print "You can't use that right now!"
    elif direction == "flee":
        print "What are you fleeing from, you coward, there's nothing there?"
    elif direction == "listen":
        print "There is nothing for you to hear."
    elif direction == "examine":
        print "There isn't anything for you to examine."
    elif direction == "commands":
        cmmdList()
    else:
        print "I don't understand that command."
    return

def stats(canvas):
    print "<------------------------------------->"
    print "These are your current stats: "
    print "Hit Points:",canvas.data.hp
    print "Defense Points",canvas.data.dp
    print "Weapon:",canvas.data.weapon
    print "Experience Points:",canvas.data.XP
    print "Inventory:",canvas.data.inventoryList
    print "<------------------------------------->"
    return

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
"""
def attack(hp, dp, monster, monsterHP, monsterDP, canvas):
     print "!----BATTLE----!"
     print "You strike at the monster and..."
     DP = canvas.data.monsterDP
     answer = "yes"
     Roll = d20()
     while hp >= 0:
          attack = Roll + hp
          if attack >= monsterDP/2:
               damage = Roll/2
               if damage > 0:
                    DP -= damage
                    print "you did", damage, "damage to the",\
                          canvas.data.monster
               else:
                    print "you miss!"
          else:
            print "you miss!"
          print "It strikes at you and..."
          mRoll = d6()
          mAttack = mRoll + monsterHP
          if mAttack >= dp/2:
               mdamage = mRoll/2
               if mdamage > 0:
                    canvas.data.hp -= mdamage
                    print "it does", mdamage," to you."
               else:
                    print "it misses you!"

          else:
               print "it misses you!"
          Roll = d20()
     print "With one final strike, you kill the", canvas.data.monster
     print "!----END BATTLE----!"
     if canvas.data.monsterGold > 0:
        canvas.data.gold += canvas.data.monsterGold
        canvas.data.monsterLives -= 1
        addtoXP = d6()
        canvas.data.XP += addtoXP
        print "You get ",canvas.data.monsterGold," gold \
     and",addtoXP,"XP."
        canvas.data.monsterGold == 0
        return
     else:
        addtoXP = d6()
        canvas.data.XP += addtoXP
        print "You earned", addtoXP,"XP."
        canvas.data.monsterLives -=1
        return
"""
def attack(hp, dp, monster, monsterHP, monsterDP, canvas):
     print "!----BATTLE----!"
     print "You strike at the monster and..."
     while canvas.data.monsterLives == 1:
          if canvas.data.hp == 0:
               gameOver(character, canvas)
          else:
               Roll = d20()
               attack = Roll + hp
               damage = Roll/2
               mRoll = d6()
               mAttack = mRoll + monsterHP
               mdamage = mRoll/2
          if canvas.data.monsterHP <= 0:
               canvas.data.monsterLives -= 1
          else:
               if attack >= monsterDP/2:
                    if damage > 0:
                         canvas.data.monsterHP -= damage
                         print "you did",damage,"damage to \
the",canvas.data.monster
                    else:
                         print "you miss!"
               else:
                    print "you miss!"
               if mAttack >= dp/2:
                    if mdamage > 0:
                         canvas.data.hp -= mdamage
                         print "it does",mdamage,"to you."
                         print "Your HP", canvas.data.hp
                    else:
                         print "it misses you!"
               else:
                    print "it misses you!"
          Roll = d20()
     print "With one final strike, you kill the", canvas.data.monster
     print "!----END BATTLE----!"
     if canvas.data.monsterGold > 0:
        canvas.data.gold += canvas.data.monsterGold
        addtoXP = d6()
        canvas.data.XP += addtoXP
        print "You get ",canvas.data.monsterGold," gold \
and",addtoXP,"XP."
        canvas.data.monsterGold == 0
        return
     else:
        addtoXP = d6()
        canvas.data.XP += addtoXP
        print "You earned", addtoXP,"XP."
        return


def isInInventory(obj,canvas):
    #wanted in a separate function
    rows = len(canvas.data.inventoryList)
    cols = len(canvas.data.inventoryList[0])
    for row in range(rows):
        for col in range(cols):
            print "obj",obj
            print "row", row, "col", col
            print "row,col", canvas.data.inventoryList[row][col]
            if obj == canvas.data.inventoryList[row][col]:
                return True
    return False

#def dropItem(canvas):
#    dropThis = raw_input("What item from your inventory would you like \
#to drop?")
#   inventoryList = canvas.data.inventoryList

def dream(character,canvas):
    if character == "paladin":
        print "The mage was there. He was laughing and looking down \
on you as you drifted into a deep sleep. He was holding Lyane in his \
arms. He was killing her. But it wasn't the mage, it was your father. \
Your father killed her, and you cast off your family name. You became a \
knight. Your dream is to become a lord and challenge your father as an equal. \
You will avenge Lyane."
        more = raw_input("Do you want to remember more? (yes or no)")
        if more == "yes":
            print "You remember lying with Lyane in the grass behind her \
father's house. Her father, pleased that the lord's son was so taken with his \
little girl, did not mind. That day, they laughed, throwing grass at each \
other and making shapes from the clouds. The next day, she was dead. \
You awake in the room, cold and alone."
        else:
            print "You don't want to remember any more, and you close your \
eyes, hoping not to see. You awake in the room, cold and alone."
    elif character == "rogue":
        print "The mage was in the room, laughing at you, his shining eyes \
watching you as you drift off to sleep. Your mother lay dead at his feet. In \
his hand was a dagger, red with her blood. You tried to scream, but the blade \
was in you too. You pressed your hand against your stomach and it comes away \
red with your blood."
        more = raw_input("Do you want to remember more? (yes or no)")
        if more == "yes":
            print "You cried. He left you there, in pain, crying. Your mother \
was already dead. As you bled into the dirt, you watched a fly land on her \
face, and crawl toward her eye. You screamed. Tried to shoo it away. It \
wouldn't go. You watched it until you couldn't keep your eyes open anymore. \
You awake in the room, cold and alone."
        else:
            print "You don't want to remeber any more; you close your eyes, \
hoping not to see. You awake in the room, cold and alone."

def addToInventory(item):
     canvas.data.inventoryList += [item]
     return

def getName(charType):
    getName = raw_input("Welcome, what is your name? ")
    return getName

def getCharType():
     charType = raw_input("You can be a paladin or a rogue. \
Which would you like? ")
     return charType

def createCharacter(canvas):
    canvas.data.character = getCharType()
    canvas.data.name = getName(canvas.data.character)
    canvas.data.hp = rollHP(canvas.data.character)
    canvas.data.dp = rollDP(canvas.data.character)
    canvas.data.weapon = firstWeapon(canvas.data.character)
    return

def firstWeapon(character):
     if character == "rogue":
          return "dagger"
     elif character == "paladin":
          return "sword"

def riverTroll(canvas):
     canvas.data.monster = "River Troll"
     canvas.data.monsterHP = random.randint(10,20)
     canvas.data.monsterDP = random.randint(10,30)
     canvas.data.monsterGold = dWithZero()
     return

def suitOfArmor(canvas):
     canvas.data.monster = "suit of armor"
     canvas.data.monsterHP = random.randint(20,30)
     canvas.data.monsterDP = random.randint(20,40)
     canvas.data.monsterGold = dWithZero()
     return

def warg(canvas):
     canvas.data.monster = "warg"
     canvas.data.monsterHP = random.randint(10,30)
     canvas.data.monsterDP = random.randint(20,50)
     canvas.data.monsterGold = dWithZero()
     return

def statue1(canvas):
     canvas.data.monster = "First Statue"
     canvas.data.monsterHP = random.randint(10,30)
     canvas.data.monsterDP = random.randint(20,50)
     canvas.data.monsterGold = dWithZero()
     return

def statue2(canvas):
     canvas.data.monster = "Second Statue"
     canvas.data.monsterHP = random.randint(20,40)
     canvas.data.monsterDP = random.randint(30,50)
     canvas.data.monsterGold = dWithZero()
     return
     
def mage(canvas):
     canvas.data.monster = "mage"
     canvas.data.monsterHP = random.randint(50,70)
     canvas.data.monsterDP = random.randint(50,80)
     canvas.data.monsterGold = d20()
     return
