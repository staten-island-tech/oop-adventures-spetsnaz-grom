print("You are a soldier in the United States Army Rangers, and you have been sent to fight in the Republic of Wadiya.")
print("You arrive at Fort Ripton, a military base in the occupied province of al hilal, and are immediately called to select your choice of gear by high command.")






class Player:
    def __init__(self):
        self.chosen_class = None
        self.points = 2000

    def choose_class(self):
        if self.chosen_class is not None:
            print("You have already chosen a class.")
        else:
            while True:
                class_choice = input("Select a class (Juggernaut, Demolition, or Assault): ").strip().capitalize()
                if class_choice in ["Juggernaut", "Demolition", "Assault"]:
                    self.chosen_class = class_choice
                    print(f"Thank you for selecting the {class_choice} class. You may now proceed.")
                    break
                else:
                    print("Invalid class selected.")

class Juggernaut:
    def __init__(self):
        self.hp = 1000
        self.speed = 10
        self.armor = 500
        self.resistance = ["bullet", "explosive"]
        self.helmet = "Altyn"

    def take_damage(self, damage_type, damage_amount):
        if damage_type in self.resistance:
            damage_amount /= 2
        self.hp -= damage_amount
        if self.hp <= 0:
            print("The Juggernaut has been defeated.")
            return True
        else:
            return False

    def check_kill(self, damage_type):
        if damage_type in ["tank", "jet", "helicopter", "gunship"]:
            print("The Juggernaut has been defeated.")
            return True
        elif damage_type == "bullet":
            self.armor -= 1
            if self.armor <= 0:
                print("The Juggernaut has been defeated.")
                return True
            else:
                return False
        elif damage_type in ["rocket", "sniper"]:
            self.hp -= 100
            if self.hp <= 0:
                print("The Juggernaut has been defeated.")
                return True
            else:
                return False

class Demolition:
    def __init__(self):
        self.hp = 50
        self.speed = 50
        self.armor = 0
        self.resistance = []
        self.weapons = ["grenade launcher", "pistol"]

    def take_damage(self, damage_type, damage_amount):
        self.hp -= damage_amount
        if self.hp <= 0:
            print("The Demolition has been defeated.")
            return True
        else:
            return False

    def check_kill(self, damage_type):
        if damage_type in ["tank", "jet", "helicopter", "gunship"]:
            print("The Demolition has been defeated.")
            return True
        elif damage_type == "bullet":
            self.hp -= 1
            if self.hp <= 0:
                print("The Demolition has been defeated.")
                return True
            else:
                return False
        elif damage_type in ["rocket", "sniper"]:
            self.hp -= 25
            if self.hp <= 0:
                print("The Demolition has been defeated.")
                return True
            else:
                return False

class Assault:
    def __init__(self):
        self.hp = 20
        self.speed = 100
        self.armor = 20
        self.resistance = []
        self.weapons = ["M4A1 assault rifle", "AWP sniper rifle", "colt 1911 pistol"]

    def take_damage(self, damage_type, damage_amount):
        self.armor -= damage_amount
        if self.armor <= 0:
            self.hp -= 1
            if self.hp <= 0:
                print("The Assault has been defeated.")
                return True
            else:
                return False
        else:
            return False

class Enemy:
    def __init__(self, name, health, points):
        self.name = name
        self.health = health
        self.points = points

    def deal_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The {self.name} has been defeated. You earned {self.points} points.")
            player.points += self.points
            return True
        else:
            return False


player = Player()
player.choose_class()

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
        self.item_descriptions = {
            'AC-130 gunship': "The vehicle version of the doom slayer",
            'MI-24 helicopter': "Nicknamed the Devil's chariot or the Flying tank, the fearsome Mi-24 lives up to its reputation as one nasty warbird",
            'Tu-95 bomber run': "An unstoppable force with firepower capable of destroying everything in its path",
            'Yak-38 VTOL jet': "A mean machine capable of dominating the skies",
            'BTR-90 APC': "A beast of a vehicle that will destroy anything in its path"
        }
        self.item_properties = {
            'AC-130 gunship': {'health': 2000, 'armor': 4000, 'damage': 5000, 'speed': 100},
            'MI-24 helicopter': {'health': 1000, 'armor': 5000, 'damage': 4000, 'speed': 300},
            'Tu-95 bomber run': {'health': 3000, 'armor': 3000, 'damage': 6000, 'speed': 200},
            'Yak-38 VTOL jet': {'health': 500, 'armor': 2000, 'damage': 5000, 'speed': 500},
            'BTR-90 APC': {'health': 4000, 'armor': 6000, 'damage': 2000, 'speed': 50}
        }

    def display_choices(self):
        for key, value in self.choices.items():
            print(f"{key}: {value} (Cost: {self.item_costs[value]} points)")

    def buy_item(self, item_choice):
        item_name = self.choices[item_choice]
        item_cost = self.item_costs[item_name]
        if player.points < item_cost:
            print("Insufficient points. Unable to make the purchase.")
            return None
        else:
            player.points -= item_cost
            print(f"You have purchased {item_name} for {item_cost} points.")
            print(f"{item_name}: {self.item_descriptions[item_name]}")
            item_properties = self.item_properties[item_name]
            print("Item properties:")
            for key, value in item_properties.items():
                print(f"{key}: {value}")
            return item_name


buy_station = BuyStation()
buy_station.display_choices()
item_choice = input("Choose an item to buy (enter the corresponding number): ")
bought_item = buy_station.buy_item(item_choice)

if bought_item:
    print(f"You have acquired {bought_item}.")
    print("Proceeding with the mission...")
   
   
class Player:
    def __init__(self, player_class):
        self.player_class = player_class
        self.health = 100
        self.weapon = None

    def choose_weapon(self):
        if self.player_class == "Assault":
            self.weapon = M4A1()
        elif self.player_class == "Sniper":
            self.weapon = AWPSniperRifle()
        elif self.player_class == "Demolition":
            self.weapon = RPG()
        elif self.player_class == "Juggernaut":
            self.weapon = Minigun()

    def shoot(self):
        if self.weapon:
            self.weapon.shoot()
        else:
            print("No weapon chosen.")

    def reload(self):
        if self.weapon:
            self.weapon.reload()
        else:
            print("No weapon chosen.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Player has been defeated.")
            return True  # Signal that the player is defeated
        return False  # Signal that the player is still alive


class Infantry:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Enemy infantry has been defeated.")
            return True  # Signal that the enemy is defeated
        return False  # Signal that the enemy is still alive


class M4A1:
    def __init__(self):
        self.range = 300
        self.damage = 50
        self.magazine_capacity = 30
        self.ammo_count = self.magazine_capacity

    def shoot(self):
        if self.ammo_count > 0:
            self.ammo_count -= 1
            print("M4A1 rifle fires and deals {} damage.".format(self.damage))
        else:
            print("M4A1 rifle is out of ammo. Reload!")

    def reload(self):
        self.ammo_count = self.magazine_capacity
        print("M4A1 rifle has been reloaded. Magazine capacity: {}".format(self.magazine_capacity))


class AWPSniperRifle:
    def __init__(self):
        self.range = 5000
        self.damage = 500
        self.ammo_capacity = 5

    def shoot(self):
        if self.ammo_capacity > 0:
            print("AWP sniper rifle shoots with {} damage.".format(self.damage))
            self.ammo_capacity -= 1
        else:
            print("AWP sniper rifle is out of ammo. Reload!")

    def reload(self):
        print("Reloading AWP sniper rifle.")
        self.ammo_capacity = 5


class RPG:
    def __init__(self):
        self.damage = 200
        self.ammo_capacity = 1

    def shoot(self):
        if self.ammo_capacity > 0:
            print("RPG fires and deals {} damage.".format(self.damage))
            self.ammo_capacity -= 1
        else:
            print("RPG is out of ammo. Reload!")

    def reload(self):
        print("Reloading RPG.")
        self.ammo_capacity = 1


class Minigun:
    def __init__(self):
        self.damage = 30

    def shoot(self):
        print("Minigun fires and deals {} damage.".format(self.damage))

    def reload(self):
        print("Minigun does not require reloading.")


player_class = input("Choose your class (Assault, Sniper, Demolition, Juggernaut): ")
player = Player(player_class)
player.choose_weapon()

enemy_count = 10
enemy = Infantry(50)

print("You arrive at the compound and are taking extremely heavy fire from the runway. You engage.")

while enemy_count > 0 and not player.take_damage(10):
    player.shoot()
    if enemy.take_damage(player.weapon.damage):
        enemy_count -= 1

print("You have mowed down all the infantry.")

for meter in range(1, 6):
    print(f"Sprinting through meter {meter}...")
    if meter == 1.5:
        print("You come across an NPC.")
        npc = NPC("Private Jackson Samuleson")
        npc.talk("Hello, soldier. I'm Private Jackson Samuleson.")
        npc.talk("I'm here to provide you with some important information.")
        npc.talk("We have spotted a 20-tank battalion moving to resecure the base.")
        npc.talk("I recommend using a killstreak to destroy them.")
   
   