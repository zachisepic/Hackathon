from commands import CheckCommands
from Dog import dog
import time
import threading
import player

run = True


threading.Thread(target=dog.hunger_decay, daemon=True).start()

dog.hunger = 100
while run:
    Player = input(f"What do you want to do with {dog.name}: ")
    CheckCommands(Player.lower())
    if (Player == 'Exit'):
        run = False
    if dog.hunger > 100:
        dog.hunger = 100
    if dog.relationship == 100:
        player.rNum += 1
        print(player.rNum)
        dog.relationship = 0