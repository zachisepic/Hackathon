from commands import CheckCommands

run = True

while run:
    player = input("Enter a command: ")
    CheckCommands(player)
    if (player == 'Exit'):
        run = False