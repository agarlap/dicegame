
import random

pos = 0

for x in range(1,11):
    print("Turn #",x,":")
    dice1 = random.randrange(1, 7)
    print("Dice 1 rolled: ", dice1)
    dice2 = random.randrange(1, 7)
    print("Dice 2 rolled: ", dice2)

    if dice1 == dice2:
        dice3 = random.randrange(1, 7)
        print("DOUBLES!")
        print("Dice 3 rolled: ", dice3)
        pos = pos + dice1 + dice2 + dice3
    else:
        pos = pos + dice1 + dice2
        
    print("Position: ",pos)

print("OVERALL POSITION:", pos)
