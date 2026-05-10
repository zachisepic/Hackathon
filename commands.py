from Dog import dog
import player
import random
from crystals import help
import dogascii
import playsound3


def CheckCommands(command):
    
    if(command == 'help'):
        playsound3.playsound('assets/bark.mp3')
        print("""
              Emotions - Check emotions
              Feed - Feed them
              Play - Play with them
              Status - Check his hunger and happiness
              Happiness - Check his happiness
              Relationship - Check how close you guys are
              Crystals - Look at all different crystal types
              Recycle - Recycle Waste
              Inventory - Check your inventory
              Exit - Leave the program

""")
    elif (command == 'crystals'):
        help()
    elif(command == 'emotions'):
        if player.eNum == 0:
            print(dogascii.alien_happy_dog)

        elif player.eNum == 2:
            print(dogascii.alien_angry_dog)
            playsound3.playsound('assets/growl.mp3')

        dog.emotion_status(player.eNum)
        
        
    
    elif(command == 'feed'):
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
        print(dogascii.alien_dog_eating)

        color = input("What color of Crystal do you pick: ")
        if color == 'Red' and player.inventory["Red Crystal"] != 0:
            dog.hunger += 20
            dog.relationship += 20
            player.eNum = 2
            playsound3.playsound('assets/eat.mp3')
            player.inventory["Red Crystal"] -= 1
        elif color == 'Green' and player.inventory["Green Crystal"] != 0:
            dog.hunger += 15
            dog.relationship += 15
            dog.happiness += 10
            playsound3.playsound('assets/eat.mp3')
            player.inventory["Green Crystal"] -= 1
        elif color == 'Orange' and player.inventory["Orange Crystal"] != 0:
            dog.hunger += 10
            dog.relationship += 10
            dog.happiness += 10
            playsound3.playsound('assets/eat.mp3')  
            player.inventory["Orange Crystal"] -= 1
        elif color == 'Blue' and player.inventory["Blue Crystal"] != 0:
            dog.hunger += 10
            dog.happiness += 10
            playsound3.playsound('assets/eat.mp3')
            player.inventory["Blue Crystal"] -= 1
        elif color == 'Yellow' and player.inventory["Yellow Crystal"] != 0:
            dog.hunger += 10
            dog.relationship += 10
            dog.happiness += 10
            player.eNum = 0
            playsound3.playsound('assets/eat.mp3')  
            player.inventory["Yellow Crystal"] -= 1
        elif color == 'White' and player.inventory["White Crystal"] != 0:
            dog.hunger += 10
            playsound3.playsound('assets/eat.mp3')
            player.inventory["White Crystal"] -= 1
        else: 
            print("You don't have that crystal or that is not a crystal")
        

    elif(command == 'relationship'):
        dog.check_relationship(player.rNum)
    elif(command == 'Status'):
        dog.status()
    elif (command == 'inventory'):
        print(player.inventory)
    elif (command == 'recycle'):
        if player.inventory["Waste"] > 0:
            player.inventory["Waste"] -= 1
            player.inventory["White Crystal"] += 1
            print(f"You got a White Crystal")
        elif (player.inventory["Waste"] > 0 and player.rNum == 3):
            r1 = random.choice(player.inventory)
            r1 += 1
            print(r1)
    elif (command == 'play'):
        print(dogascii.alien_chilling_dog)
        print(f"You played with {dog.name}")
        playsound3.playsound('assets/play.mp3')
        dog.happiness += 10
        dog.relationship += 10
        
    else:
        print("Not an option type 'Help' to see list of different options")


