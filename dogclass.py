import sys


class VirtualDog:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.relationship = 0
        self.emotions= ["happy", "sad", "mad", "silly","energetic"]
        self.relations=["Strangers", "Friendly", "Companion", "Trusted", "Loyal", "Devoted", "Soul Bound"]
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

    def check_relationship(self, rNum):
        if self.relationship >= 100:
            print(f"You have beeen kind to me in return I'll tell you anything about your home planet!")
            print("""
            Pick a topic:
                  A: For History
                  B: For Biology
            """)
            self.relationship = 0
            self.relations[rNum]