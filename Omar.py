import uuid 
import time

class Basic:
    def __init__(self, id, tag, jet):
        self.id = id
        self.name = tag
        self.jet = jet
        self.tank = tank
        self.gunship = gunship
        
class tank(Basic):
    def __init__(self,id,tag,tank,explosives):
        super().__init__(self,id,tag)
        self.explosives = explosives
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.explosives}"
    
class Speedjet(Basic):
    def __init__(self,id,tag,jet,Boost):
        super().__init__(self,id,tag)
        self.Boost = Boost
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.Boost}"
    
    
class gunship(Basic):
    def __init__(self,id,tag,gunship,dropbombs):
        super().__init__(self,id,tag)
        self.dropbombs = dropbombs
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.dropbombs}"
    
class enemycar1(Basic):
    def __init__(self,id,tag,enemy1,boost2):
        super().__init__(self,id,tag)
        self.boost2 = boost2
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.boost2}"
    
class enemycar2(Basic):
    def __init__(self,id,tag,enemy1,boost3):
        super().__init__(self,id,tag)
        self.boost2 = boost3
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.boost3}"
    
class FordMustang(Basic):
    def __init__(self,id,tag,enemy1,nitro):
        super().__init__(self,id,tag)
        self.nitro = nitro 
    def __str__(self):
        return f"{self.name}, {self.jet}, {self.id}, {self.tag} {self.nitro}"
    
tank = []
Speedjet= []
enemycar1 = []
enemycar2 =[]
FordMustang = []
gunship = {}

print("choose your vehicle")
time.sleep(1)

#possible intro 

print









#first choice

choice1 = input("A) tank B) SpeedJet C) gunship: ")

if choice1.lower() == "a":
    print(" You chose tank, you unlocked attachment: explosives. (press 9 to activate 2 uses)")
    time.sleep(1)
    print(" Equipped with your new tank you drive out to scout the land.")
    time.sleep(1)
  
    
elif choice1.lower() == "b":
    print("  You chose SpeedJet, you unlocked attachment: Boost. (press 0 to activate 2 uses) ")
    time.sleep(1)
    print(" Equipped with your new Jet you fly out to scout the skies. ")
    time.sleep(1)


elif choice1.lower() == "c":
    print("  You chose gunship, you unlocked attachment: dropbombs. (press 8 to activate 2 uses) ")
    time.sleep(1)
    print(" Equipped with your new gunship you fly out to scout the skies. ")
    time.sleep(1)

customize_your_jet = "Y"


































