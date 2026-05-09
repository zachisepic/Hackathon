import sys
import fact
import time
from player import inventory


class VirtualDog:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.relationship = 0
        self.emotions= ["happy", "sad", "mad", "silly","energetic"]
        self.relations=["Strangers", "Friendly", "Companions", "Trusted", "Loyal", "Devoted", "Soul Bound"]
    def emotion_status(self, EmotionNum):
        print(f"{self.name} is currently feeling {self.emotions[EmotionNum]}.")
    
    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        print(f"{self.name} has been fed. Hunger: {self.hunger}")

    def play(self):
        if self.hunger < 50:
            self.happiness = min(100, self.happiness + 20)
            print(f"{self.name} is playing. Happiness: {self.happiness}")
        else:
            print(f"{self.name} is too hungry to play.")

    def status(self):
        print(f"{self.name}'s Status - Hunger: {self.hunger}, Happiness: {self.happiness}")

    def check_happiness(self):
        if self.happiness >= 80:
            print(f"{self.name} is very happy!")
        elif self.happiness >= 50:
            print(f"{self.name} is moderately happy.")
        else:
            print(f"{self.name} is not very happy.")
    def hunger_decay(self):
        while True:
            time.sleep(120)
            self.hunger -= 10
            self.waste()
            if self.hunger <= 30:
                self.relationship -= 10
            else:
                self.relationship += 5
    
    def waste(self):
        print(f"\n{self.name} has relieved itself.")
        inventory["Waste"] += 2
        
    def check_relationship(self, rNum):
        print(f"{self.name} considers you a {self.relations[rNum]} with a relationship score of {self.relationship}.")
        if self.relationship >= 0:
            print(f"You have beeen kind to me in return I'll tell you anything about your home planet!")
            print("""
                Pick a Topic
                  A: For History
                  B: For Biology
                  C: For Geography""")
            self.relations[rNum]
            option = input("Option: ")
            if option == "A" and rNum == 0:
                print(fact.history1)
            elif option == "B" and rNum == 0:
                print(fact.biology1)
            elif option == "C" and rNum == 0:
                print(fact.geography1)
            elif option == "A" and rNum == 1:
                print(fact.history2)
            elif option == "B" and rNum == 1:
                print(fact.biology2)
            elif option == "C" and rNum == 1:
                print(fact.geography2)
            elif option == "A" and rNum == 2:
                print(fact.history3)
            elif option == "B" and rNum == 2:
                print(fact.biology3)
            elif option == "C" and rNum == 2:
                print(fact.geography3)
            elif option == "A" and rNum == 3:
                print(fact.history4)
            elif option == "B" and rNum == 3:
                print(fact.biology4)
            elif option == "C" and rNum == 3:
                print(fact.geography4)
            elif option == "A" and rNum == 4:
                print(fact.history5)
            elif option == "B" and rNum == 4:
                print(fact.biology5)
            elif option == "C" and rNum == 4:
                print(fact.geography5)
            elif option == "A" and rNum == 5:
                print(fact.history6)
            elif option == "B" and rNum == 5:
                print(fact.biology6)
            elif option == "C" and rNum == 5:
                print(fact.geography6)
            elif option == "A" and rNum == 6:
                print(fact.history7)
            elif option == "B" and rNum == 6:
                print(fact.biology7)
            elif option == "C" and rNum == 6:
                print(fact.geography7)


                   