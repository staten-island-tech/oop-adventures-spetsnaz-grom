print("You are a soldier in the United States Army Rangers, and you have been sent to fight in the Republic of Wadiya.")
print("You arrive at Fort Ripton, a military base in the occupied province of al hilal, and are immediately called to select your choice of gear by high command.")

class Player:
    def __init__(self):
        self.chosen_class = None
        self.points = 2000
    
    def choose_class(self):
        if self.chosen_class is not None:
            print("You have already chosen a class.")
            return

class Juggernaut:
    def __init__(self):
        self.hp = 1000
        self.speed = 10 # Juggernaut is slow
        self.armor = 500 # Juggernaut has a minigun with a 500 round ammo reserve
        self.resistance = ["bullet", "explosive"]
        self.helmet = "Altyn"
    
    def take_damage(self, damage_type, damage_amount):
        if damage_type in self.resistance:
            damage_amount /= 2 # Resistance reduces damage by half
        self.hp -= damage_amount
        if self.hp <= 0:
            print("The Juggernaut has been defeated.")
            return True # Player has been killed
        else:
            return False # Player is still alive
    
    def check_kill(self, damage_type):
        if damage_type in ["tank", "jet", "helicopter", "gunship"]:
            print("The Juggernaut has been defeated.")
            return True # Player has been killed
        elif damage_type == "bullet":
            self.armor -= 1
            if self.armor <= 0:
                print("The Juggernaut has been defeated.")
                return True # Player has been killed
            else:
                return False # Player is still alive
        elif damage_type in ["rocket", "sniper"]:
            self.hp -= 100 # Rocket launchers and snipers deal 100 damage per shot
            if self.hp <= 0:
                print("The Juggernaut has been defeated.")
                return True # Player has been killed
            else:
                return False # Player is still alive

class Demolition:
    def __init__(self):
        self.hp = 50
        self.speed = 50 # Demolition is the second fastest class
        self.armor = 0 # Demolition is lightly armored
        self.resistance = []
        self.weapons = ["grenade launcher", "pistol"]
    
    def take_damage(self, damage_type, damage_amount):
        self.hp -= damage_amount
        if self.hp <= 0:
            print("The Demolition has been defeated.")
            return True # Player has been killed
        else:
            return False # Player is still alive
    
    def check_kill(self, damage_type):
        if damage_type in ["tank", "jet", "helicopter", "gunship"]:
            print("The Demoman has been defeated.")
            return True # Player has been killed
        elif damage_type == "bullet":
            self.hp -= 1 # Handheld bullet weapons take 50 shots to kill
            if self.hp <= 0:
                print("The Demoman has been defeated.")
                return True # Player has been killed
            else:
                return False # Player is still alive
        elif damage_type in ["rocket", "sniper"]:
            self.hp -= 25 # Rocket launchers and snipers deal 25 damage per shot
            if self.hp <= 0:
                print("The Demolition has been defeated.")
                return True # Player has been killed
            else:
                return False # Player is still alive

class Assault:
    def __init__(self):
        self.hp = 20
        self.speed = 100 # Assault is the fastest class
        self.armor = 20 # Assault has 20 hp of armor
        self.resistance = []
        self.weapons = ["M4A1 assault rifle", "AWP sniper rifle", "colt 1911 pistol"]
    
    def take_damage(self, damage_type, damage_amount):
        self.armor -= damage_amount
        if self.armor <= 0:
            self.hp -= 1 # Once armor is depleted, player takes damage to hp
            if self.hp <= 0:
                print("The Assault has been defeated.")
                return True # Player has been killed
            else:
                return False # Player is still alive
        else:
            return False # Player is still alive

class Enemy:
    def __init__(self, name, health, points):
        self.name = name
        self.health = health
        self.points = points
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The {self.name} has been defeated. You earned {self.points} points.")
            player.points += self.points
            return True # Enemy has been killed
        else:
            return False # Enemy is still alive

player = None

while True:
    class_choice = input("Select a class (Juggernaut, Demolition, or Assault): ").strip().capitalize()
    if class_choice in ["Juggernaut", "Demolition", "Assault"]:
        player = Player()
        if class_choice == "Juggernaut":
            player.chosen_class = Juggernaut()
        elif class_choice == "Demolition":
            player.chosen_class = Demolition()
        elif class_choice == "Assault":
            player.chosen_class = Assault()
        print(f"Thank you for selecting the {class_choice} class. You may now proceed.")
        break
    else:
        print("Invalid class selected.")

print("After selecting a class, you are deployed to secure a heavily armed Wadiyan objective.")
print("The objective is a fortified compound in the middle of Al hilal. It is a major strategic point that must be captured.")

for mile in range(1, 6):
    print(f"Driving through mile {mile}...")
    if mile == 1:
        choice = input("You come across an NPC. Do you want to interact with him? (Y/N): ").strip().capitalize()
        if choice == "Y":
            print("You decide to interact with the NPC.")
            print("NPC: Hello, American soldier. This here is a buystation. Let me tell you how it works.")
            print("NPC: You can use the buystation by pressing the B key to interact with it.")
            print("NPC: To make a purchase, press the A key.")
            print("NPC: Each buystation buy costs 2000 points.")
            print("NPC: Good luck in your battle against terrorism!")
        else:
            print("You choose not to interact with the NPC and continue your mission.")
    else:
        pass


print("You arrive at a hill overlooking the base, and you see a buystation. Buy a kill streak from the buystation to proceed.")

class BuyStation:
    def __init__(self):
        self.choices = {
            '1': 'AC-130 gunship',
            '2': 'MI-24 helicopter',
            '3': 'Tu-95 bomber run',
            '4': 'Yak-38 VTOL jet',
            '5': 'BTR-90 APC'
        }
        self.item_costs = {
            'AC-130 gunship': 2000,
            'MI-24 helicopter': 2000,
            'Tu-95 bomber run': 2000,
            'Yak-38 VTOL jet': 2000,
            'BTR-90 APC': 2000
        }
        self.points = 0

    def display_menu(self):
        print("Buy Station Menu:")
        for choice, item in self.choices.items():
            print("{}: {}".format(choice, item))

    def interact(self):
        while True:
            choice = input("Press B to interact with the Buy Station (or Q to quit): ")
            if choice.upper() == 'B':
                self.display_menu()
                self.buy()
            elif choice.upper() == 'Q':
                print("Exiting Buy Station.")
                break
            else:
                print("Invalid choice. Please try again.")

    def buy(self):
        while True:
            item = input("Enter the number of the item you want to buy (or Q to quit): ")
            if item.upper() == 'Q':
                print("Exiting buy menu.")
                break
            elif item in self.choices:
                selected_item = self.choices[item]
                cost = self.item_costs[selected_item]
                if player.points >= cost:
                    print("You bought: {}".format(selected_item))
                    player.points -= cost
                    print("Points remaining: {}".format(player.points))
                    self.process_purchase(selected_item)
                else:
                    print("Insufficient points to buy the item.")
            else:
                print("Invalid choice. Please try again.")

    def process_purchase(self, item):
        if item == 'AC-130 gunship':
            # Logic for spawning AC-130 gunship
            print("AC-130 gunship deployed. Prepare for air support.")
        elif item == 'MI-24 helicopter':
            # Logic for spawning MI-24 helicopter
            print("MI-24 helicopter deployed. Air support inbound.")
        elif item == 'Tu-95 bomber run':
            # Logic for initiating Tu-95 bomber run
            print("Tu-95 bomber run initiated. Stand clear of the target area.")
        elif item == 'Yak-38 VTOL jet':
            # Logic for spawning Yak-38 VTOL jet
            print("Yak-38 VTOL jet deployed. Air superiority achieved.")
        elif item == 'BTR-90 APC':
            # Logic for spawning BTR-90 APC
            print("BTR-90 APC deployed. Ground support en route.")

buy_station = BuyStation()

while True:
    buy_station.interact()
    if player.points < 2000:
        print("Insufficient points to buy further items.")
        break

print("You have successfully acquired the necessary equipment. Proceed with the mission.")


