from commands import CheckCommands
from Dog import dog

run = True



while run:
    player = input("Enter a command: ")
    CheckCommands(player)
    if (player == 'Exit'):
        run = False
    if dog.hunger > 100:
        dog.hunger = 100