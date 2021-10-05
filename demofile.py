
import random

pos = 0

for x in range(1,11):
    print("Turn #",x,":")
    dice1 = random.randrange(1, 7)
    print("Dice 1 rolled: ", dice1)
    pos = pos + dice1
    print("Position: ",pos)

print("OVERALL POSITION:", pos)
