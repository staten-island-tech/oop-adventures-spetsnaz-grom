import uuid 
import time

class Basic:
    def __init__(self, id, tag, jet):
        self.id = id
        self.name = tag
        self.jet = jet
        
class fighterjet(Basic):
    def __init__(self,id,tag,jet,Minigun):
        super().__init__(self,id,tag)
        self.Minigun = Minigun
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.Minigun}"
    
class Speedjet(Basic):
    def __init__(self,id,tag,jet,Boost):
        super().__init__(self,id,tag)
        self.Boost = Boost
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.Boost}"
    
    
class Stealthjet(Basic):
    def __init__(self,id,tag,jet,Cloak):
        super().__init__(self,id,tag)
        self.Cloak = Cloak
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.Cloak}"
    
fighterjet = []
Stealthjet = []
Stealthjet = {}

print("choose your fighter")
time.sleep(1)

#first choice



choice1 = input("A) FighterJet B) SpeedJet C) StealthJet: ")

if choice1.lower() == "a":
    print(" You chose FighterJet, you unlocked attachment: Minigun. (press 9 to activate 2 uses)")
    time.sleep(1)
    print(" Equipped with your new Jet you fly out to scout the skies.")
    time.sleep(1)
  
    
elif choice1.lower() == "b":
    print("  You chose SpeedJet, you unlocked attachment: Boost. (press 0 to activate 2 uses) ")
    time.sleep(1)
    print(" Equipped with your new Jet you fly out to scout the skies. ")
    time.sleep(1)


elif choice1.lower() == "c":
    print("  You chose StealthJet, you unlocked attachment: Cloak. (press 8 to activate 2 uses) ")
    time.sleep(1)
    print(" Equipped with your new Jet you fly out to scout the skies. ")
    time.sleep(1)

customize_your_jet = "Y"




















































