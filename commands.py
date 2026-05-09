from Dog import dog
import player
import random



def CheckCommands(command):
    
    if(command == 'help'):
        print("""
              Emotions - Check emotions
              Feed - Feed them
              Play - Play with them
              Status - Check his hunger and happiness
              Happiness - Check his happiness
              Relationship - Check how close you guys are
              Crystals - Look at all different crystal types
              Recycle - Recycle Waste
              Exit - Leave the program

""")
    elif(command == 'Emotions'):
        dog.emotion_status(1)
    
    elif(command == 'Feed'):
        print("What kind of crystal do you want to give it:")
        print("""
        All crystals:
        Red Crystal
        Green Crystal
        Orange Crystal
        Blue Crystal
        Yellow Crystal
        White Crystal
        
        """)
        color = input("What color of Crystal do you pick: ")
        
    elif(command == 'Relationship'):
        dog.check_relationship(player.rNum)
    elif(command == 'Status'):
        dog.status()
    elif (command == 'Inventory'):
        print(player.inventory)
    elif (command == 'Recycle'):
        if player.inventory["Waste"] > 0:
            player.inventory["Waste"] -= 1
            player.inventory["White Crystal"] += 1
            print(f"You got a White Crystal")
        elif (player.inventory["Waste"] > 0 and player.rNum == 3):
            r1 = random.choice(player.inventory)
            r1 += 1
            print(r1)
            


