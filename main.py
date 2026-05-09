from commands import CheckCommands, rNum
from Dog import dog
import time
import threading
run = True

inventory = {
    "Red Crystal": 0,
    "Green Crystal": 0,
    "Orange Crystal": 0,
    "Blue Crystal": 0,
    "Yellow Crystal": 0,
    "White Crystal": 3,

    "Waste": 0,
}
rNum = 0

threading.Thread(target=dog.hunger_decay, daemon=True).start()
dog.hunger = 100
while run:
    player = input("Enter a command: ")
    CheckCommands(player)
    if (player == 'Exit'):
        run = False
    if dog.hunger > 100:
        dog.hunger = 100
    if dog.relationship == 100:
        rNum += 1