import uuid 
import time

class Basic:
    def __init__(self, id, tag, enemycar1, enemycar2, FordMustang, DodgeCharger, LamborghiniA):
        self.id = id
        self.name = tag
        self.enemycar1 = enemycar1
        self.enemycar2 = enemycar2 
        self.FordMustang = FordMustang 
        self.DodgeCharger = DodgeCharger 
        self.LamborghiniA = LamborghiniA
    
class enemycar1(Basic):
    def __init__(self,id,tag,enemy1,boost2):
        super().__init__(self,id,tag)
        self.Enemyboost2 = boost2
    def __str__(self):
        return f"{self.name}, {self.id}, {self.tag} {self.boost2}"
    
class enemycar2(Basic):
    def __init__(self,id,tag,enemy2,boost3):
        super().__init__(self,id,tag)
        self.enemyboost3 = boost3
    def __str__(self):
        return f"{self.name}, {self.id}, {self.tag} {self.boost3}"
    
class FordMustang(Basic):
    def __init__(self,id,tag,FordMustang,nitro):
        super().__init__(self,id,tag)
        self.nitro = nitro 
    def __str__(self):
        return f"{self.name}, {self.id}, {self.tag} {self.nitro} {self.FordMustang}"
    def __str__(self):
        return "Ford Mustang Boss 429"
    
class DodgeCharger(Basic):
    def __init__(self,id,tag,DodgeCharger,nitro2):
        super().__init__(self,id,tag)
        self.nitro2 = nitro2
    def __str__(self):
        return f"{self.name}, {self.id}, {self.tag} {self.nitro2} {self.DodgeCharger}"
    def __str__(self):
        return "Dodge Charger 1978"
    
class LamborghiniA(Basic):
    def __init__(self,id,tag,LamborghiniA,nitro3):
        super().__init__(self,id,tag)
        self.nitro3 = nitro3
    def __str__(self):
        return f"{self.name}, {self.id}, {self.tag} {self.nitro3} {self.LamborghiniA}"
    def __str__(self):
        return "Lamborghini Aventador"
    
enemycar1 = []
enemycar2 =[]
FordMustang = []
DodgeCharger = []
LamborghiniA = []

#possible intro 
def intro():
    print("welcome to racer,")
    time.sleep(2)
    print("in this game you are a underground racer named alex trying to make it big")
    time.sleep(2)
    print("to make it big you need to defeat the final boss in a race to gain reputation")
    time.sleep(2)
    print("by going through diffrent levels of enemys you will be able to gain enough rapport for the boss to notice you")
    time.sleep(2)
    print("when you fight the final boss youre gonna need a good car ")
    time.sleep(2)
    print("so you can upgrade your car along the way to help your chances of winning, you will gain money from won races ")
    time.sleep(2)
    print("every win brings you closer to being a legend, are you up for the challange?")
    print("                                                                                 ")

intro()

#first choice
def select_car_intro():
    time.sleep(3)
    print("along the way you will have me your personal ai named bob, whenever you need help or explanations i will be there to help")
    time.sleep(2)
    print("now before you start to race you need a car, good thing i have these three cars from previous legends to help you get started")
    time.sleep(2)
    print("choose whichever one you like and there stats will list after, you can choose by entering the correspoding number with the car you want")
    print("                                                                                 ")
    time.sleep(2)
    
select_car_intro()

def select_Car():
    print("1. Ford Mustang Boss 429")
    print("2. Dodge Charger 1978")
    print("3. Lamborghini Aventador")
    
    choice1 = int(input("Choose wisely by entering the number of your choice: "))

    if choice1 == 1:
        user_car = FordMustang()
        print("You chose Ford Mustang, a classic car and a great choice. Here are some basic stats:")
        time.sleep(2)
        print("429 cubic-inch V8 engine, 375 horsepower, four-speed manual transmission, top speed of 150 mph.")
        time.sleep(1)

    elif choice1 == 2:
        user_car = DodgeCharger()
        print("You chose Dodge Charger, iconic and classic. Let me give you the rundown of this beast:")
        time.sleep(2)
        print("318 cubic-inch 400 V8 engine, 230 horsepower, four-speed manual transmission, top speed of 125 mph.")
        time.sleep(1)

    elif choice1 == 3:
        user_car = LamborghiniA()
        print("You chose Lamborghini, a flashy choice sure to make some heads turn. Here are some stats:")
        time.sleep(2)
        print("396.5 cubic-inches 6.5-liter V12 engine, 759 horsepower, seven-speed ISR transmission, top speed of 217 mph.")
        time.sleep(1)

    else:
        print("Error: Please choose 1, 2, or 3.")
        return select_Car()
    
    print("Great choice choosing the", user_car)
    print("Let's get you racing!")

select_Car()
 #first race

time.sleep(3)
print("you will be racing two low level racers, should be an easy win, just keeep your eyes on the road")
time.sleep(2)
print("instructions: to move the car you will be asked diffrent questions, getting them right will result in accelaration ")
time.sleep(2)
print("wrong answers will result in slowing down, now get ready ")
time.sleep(2)
print(" the race starts and your in second place use nitro?")



