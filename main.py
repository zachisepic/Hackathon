from commands import CheckCommands
import time
run = True



while run:
    player = input("Enter a command: ")
    CheckCommands(player)
    if (player == 'Exit'):
        run = False
    if dog.hunger > 100:
        dog.hunger = 100