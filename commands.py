from Dog import dog


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
        