print("You are a soldier in the United States Army Rangers, and you have been sent to fight in the Republic of Wadiya.")
print("You arrive at Fort Ripton, a military base in the occupied province of al hilal, and are immediately called to select your choice of gear by high command.")




class Player:
    def __init__(self):
        self.chosen_class = None
        self.points = 2000





class Juggernaut:
    def __init__(self):
        self.hp = 1000
        self.speed = 10
        self.armor = 500
        self.resistance = ["bullet", "explosive"]
        self.helmet = "Altyn"
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


class Demolition:
    def __init__(self):
        self.hp = 50
        self.speed = 50
        self.armor = 0
        self.resistance = []
        self.weapons = [GrenadeLauncher(), Pistol()]

    def shoot(self):
        for weapon in self.weapons:
            weapon.shoot()

    def reload(self):
        for weapon in self.weapons:
            weapon.reload()


class Assault:
    def __init__(self):
        self.hp = 20
        self.speed = 100
        self.armor = 20
        self.resistance = []
        self.weapons = [M4A1(), AWPSniperRifle(), Colt1911Pistol()]

    def shoot(self):
        for weapon in self.weapons:
            weapon.shoot()

    def reload(self):
        for weapon in self.weapons:
            weapon.reload()


class Minigun:
    def __init__(self):
        self.damage = 30

    def shoot(self):
        print("Minigun fires and deals {} damage.".format(self.damage))

    def reload(self):
        print("Minigun does not require reloading.")


class M4A1:
    def __init__(self):
        self.range = 300
        self.damage = 50
        self.magazine_capacity = 30
        self.ammo_count = self.magazine_capacity

    def shoot(self):
        if self.ammo_count > 0:
            self.ammo_count -= 1
            print("M4A1 assault rifle fires and deals {} damage.".format(self.damage))
        else:
            print("M4A1 assault rifle is out of ammo. Reload!")

    def reload(self):
        self.ammo_count = self.magazine_capacity
        print("M4A1 assault rifle has been reloaded. Magazine capacity: {}".format(self.magazine_capacity))


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


class Colt1911Pistol:
    def __init__(self):
        self.range = 50
        self.damage = 30
        self.magazine_capacity = 7
        self.ammo_count = self.magazine_capacity

    def shoot(self):
        if self.ammo_count > 0:
            self.ammo_count -= 1
            print("Colt 1911 pistol fires and deals {} damage.".format(self.damage))
        else:
            print("Colt 1911 pistol is out of ammo. Reload!")

    def reload(self):
        self.ammo_count = self.magazine_capacity
        print("Colt 1911 pistol has been reloaded. Magazine capacity: {}".format(self.magazine_capacity))


class GrenadeLauncher:
    def __init__(self):
        self.damage = 200

    def shoot(self):
        print("Grenade launcher fires and deals {} damage.".format(self.damage))

    def reload(self):
        print("Grenade launcher does not require reloading.")


class Pistol:
    def __init__(self):
        self.range = 50
        self.damage = 40
        self.magazine_capacity = 10
        self.ammo_count = self.magazine_capacity

    def shoot(self):
        if self.ammo_count > 0:
            self.ammo_count -= 1
            print("Pistol fires and deals {} damage.".format(self.damage))
        else:
            print("Pistol is out of ammo. Reload!")

    def reload(self):
        self.ammo_count = self.magazine_capacity
        print("Pistol has been reloaded. Magazine capacity: {}".format(self.magazine_capacity))


class Player:
    def __init__(self):
        self.chosen_class = None

    def choose_class(self):
        if self.chosen_class is not None:
            print("You have already chosen a class.")
        else:
            while True:
                class_choice = input("Select a class (Juggernaut, Demolition, or Assault): ").strip().capitalize()
                if class_choice == "Juggernaut":
                    self.chosen_class = Juggernaut()
                    print("Thank you for selecting the Juggernaut class. You may now proceed.")
                    break
                elif class_choice == "Demolition":
                    self.chosen_class = Demolition()
                    print("Thank you for selecting the Demolition class. You may now proceed.")
                    break
                elif class_choice == "Assault":
                    self.chosen_class = Assault()
                    print("Thank you for selecting the Assault class. You may now proceed.")
                    break
                else:
                    print("Invalid class selected.")

    def shoot(self):
        if self.chosen_class:
            self.chosen_class.shoot()
        else:
            print("No class chosen.")

    def reload(self):
        if self.chosen_class:
            self.chosen_class.reload()
        else:
            print("No class chosen.")


player = Player()
player.choose_class()
player.shoot()
player.reload()


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
   
   
class Infantry:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Enemy infantry has been defeated.")
            return True  # Signal that the enemy is defeated
        return False  # Signal that the enemy is still alive

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
   
   

import time

class Armatatank:
    def __init__(self, armor, health, damage):
        self.armor = armor
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        total_damage = damage - self.armor
        if total_damage > 0:
            self.health -= total_damage
            if self.health <= 0:
                return True  # Tank destroyed
        return False

# Assume you have already activated the killstreak

tanks = []
for _ in range(20):
    tanks.append(Armatatank(4000, 1000, 300))

tank_count = len(tanks)
points = 0
start_time = time.time()

while tank_count > 0:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= 5:
        # Every 5 seconds, an anti-air missile is launched
        # and deals damage to the killstreak
        player.take_damage(300)
        start_time = current_time
def engage_tanks(player):
    tank_count = len(tanks)
    
    while True:
        command = input("Enter a command (fire/quit): ")
        
        if command == "quit":
            break
        
        if command == "fire":
            tank_index = random.randint(0, tank_count - 1)
            tank = tanks[tank_index]
            destroyed = tank.take_damage(player.killstreak_damage)

            if destroyed:
                del tanks[tank_index]
                tank_count -= 1
                player.points += 100
                print(f"A T-14 has been destroyed. Total points: {player.points}")

            if tank_count == 0:
                print("All Armata tanks have been destroyed.")
                break
    
    print("Mission complete. Your killstreak flies away.")
    print(f"You earned {player.points} points. Total points: {player.points}")

def return_to_base():
    print("\nYour killstreak flies away and the mission ends.")
    print("You return back to base.")

# Example usage
player = Player()
engage_tanks(player)
return_to_base()





class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

class ArmoredEnemy(Enemy):
    def __init__(self):
        super().__init__(600, 200)
        self.armor = 300

def defend_wave(num_enemies, num_armored_enemies, points):
    enemies = [Enemy(300, 200) for _ in range(num_enemies)]
    armored_enemies = [ArmoredEnemy() for _ in range(num_armored_enemies)]
    defeated_enemies = 0
    defeated_armored_enemies = 0
    health = 1000

    print("Wave started! Defend against the enemies.")

    while defeated_enemies < num_enemies or defeated_armored_enemies < num_armored_enemies:
        print("\nWhat do you want to do?")
        print("1. Type 'explosives' to set explosives and ambush")
        print("2. Type 'PKM' to attack with an abandoned PKM")

        choice = input("Enter your choice: ")

        if choice == "explosives":
            print("You set explosives and wait for the enemies.")

            time.sleep(5)

            print("The explosives detonate, taking out a group of enemies.")

            defeated_enemies += 5
        elif choice == "PKM":
            print("You pick up the abandoned PKM and start firing.")

            while defeated_enemies < num_enemies:
                fire_choice = input("Press 'F' to fire the PKM: ")

                if fire_choice == "F":
                    enemies[defeated_enemies].health -= 200

                    if enemies[defeated_enemies].health <= 0:
                        print("Enemy defeated!")
                        points += 20
                        defeated_enemies += 1
                else:
                    print("Invalid input. The enemies overpower you.")
                    return points

                time.sleep(0.1)

                for enemy in enemies:
                    health -= enemy.damage

                if health <= 0:
                    print("You are overwhelmed by the enemies. Mission failed.")
                    return points

                if defeated_enemies % 5 == 0:
                    print("One of the enemies fires at you, dealing 200 damage.")
                    health -= 200

                if defeated_enemies % 8 == 0:
                    print("Your health regenerates by 30 points.")
                    health += 30

                if health > 1000:
                    health = 1000
        else:
            print("Invalid input. The enemies overpower you.")
            return points

    print("Wave completed! Proceeding to the next phase.")

    return points

def interact_with_buystation(points):
    print("\nInteracting with the buystation.")

    choice = input("Type 'A' to activate the buystation: ")

    if choice != "A":
        print("No killstreak purchased.")
        return points

    print("Killstreak purchased!")

    # Add logic to purchase and use killstreak

    return points

def exfil():
    print("\nA CH-53 arrives to exfil you.")
    print("You board the helicopter and leave the area.")



    points = defend_wave(25, 0, points)
    points = interact_with_buystation(points)
    points = defend_wave(50, 10, points)
    exfil()



def interrogation():
    print("You find yourself in an interrogation room, facing General Mohammed Karim.")

    answer_1 = input("General Karim asks you, 'Who is the spy in the camp, nicknamed 'Rostov-1'?'\n"
                     "A) Myself\n"
                     "B) Ruslan Pelishkov\n"
                     "C) The messenger is dead\n"
                     "Enter your choice (A, B, or C): ")

    if answer_1 == "A":
        print("General Karim: 'Congratulations, you have answered correctly.'")
    else:
        print("General Karim: 'You have made a grave mistake.'")

        if answer_1 == "B" or answer_1 == "C":
            print("General Karim: 'Since you failed to provide the correct answer, an innocent man with a family must pay the price.'")
            print("The general hits you with a revolver, and you witness the death of another man.")

        print("General Karim: 'Now, tell me, who stole the key to the prison armory?'")

        answer_2 = input("A) It was Ruslan\n"
                         "B) It was the guard who misplaced it\n"
                         "C) I will not tell you\n"
                         "Enter your choice (A, B, or C): ")

        if answer_2 == "A" or answer_2 == "B":
            print("General Karim: 'Just know you are responsible for the lives that are lost.'")
            print("The general hits you with a revolver, and another innocent man loses his life.")
        else:
            print("General Karim: 'Your defiance will have consequences.'")
            print("The general puts you into a chokehold, but suddenly an explosion rocks the building.")
            print("General Karim is forced to release you and flee the scene.")

def prison_escape():
    print("After the explosion, chaos ensues in the prison. The opportunity for escape arises, and you escape.")

    
interrogation()
prison_escape()

def armory():
    print("You reach the armory and have a choice of weapons.")

    print("1) AK-47: 30 rounds, deals 60 damage, reload time: 3 seconds")
    print("2) Svd-63: 10 rounds, deals 120 damage, reload time: 5 seconds")

    weapon_choice = input("Enter the number of the weapon you want to wield (1 or 2): ")

    if weapon_choice == "1":
        weapon = "AK-47"
        ammo = 30
        damage = 60
        reload_time = 3
    elif weapon_choice == "2":
        weapon = "Svd-63"
        ammo = 10
        damage = 120
        reload_time = 5
    else:
        print("Invalid choice. Defaulting to AK-47.")
        weapon = "AK-47"
        ammo = 30
        damage = 60
        reload_time = 3

    print("You have chosen the", weapon)

def prison_run():
    print("You quickly run through the prison, encountering 6 enemies.")

 

    print("After dealing with the enemies, you enter another room and are attacked by a Wadiyan Soldier.")

    

def rescue_mission():
    print("Just as the Wadiyan Soldier is about to shoot you, he is shot by Spetsnaz Gru team members who have come to rescue you.")

    print("With their help, you run through the base, eliminating enemies along the way.")

    print("You reach a MI-24 helicopter and prepare to fly away.")

    print("As you take off, the pilot and gunner suffer heart attacks and die.")

    print("You and Ruslan throw the dead soldiers overboard and you take control of the gun.")

    print("You spot four targets and must choose which ones to attack.")

    print("A) Patriot missile site")
    print("B) Convoy of enemies")
    print("C) Parked F-14")
    print("D) T-14 Armata")

    target_choice = input("Enter the letter of the target you want to attack (A, B, C, or D): ")

    if target_choice == "A" or target_choice == "C":
        print("You successfully destroy the target and avoid getting hit by attackers. You make it out alive.")
    else:
        print("You are unable to avoid the attackers and get hit by a missile. You barely survive.")

armory()
prison_run()
rescue_mission()

import time

def dialog(message):
    print(message)
    time.sleep(2)

def arrest_player():
    print("General: You are under arrest for treason and espionage.")
    print("General: You have been assisted by a foreign hostile nation in a mission that you know was wrong!")
    print("General: You have caused the Wadiyans to become more ruthless to our soldiers, and me personally I think that’s a little selfish, don’t you think?")
    print("General: Choose your response:")
    print("A) The Wadiyans are barbarians and they were always ruthless.")
    print("B) Spit at the general and call him a muppet.")
    print("C) You don’t care for anybody except yourself.")

    choice = input("Your choice: ")

    if choice == "A":
        dialog("General: They are not barbarians, they are freedom fighters. Imagine Russia invading us tomorrow and taking over our land. How would you like that?")
        print("Choose your response:")
        print("A) They are bloody terrorists and deserve to be massacred.")
        print("B) Spit at the general.")
        print("C) The Russians are too smart to cause a World War.")

        choice = input("Your choice: ")

        if choice == "A" or choice == "C":
            dialog("General: You are more than just a war criminal. You are the definition of evil itself, and you will pay for your crimes.")
            dialog("The General kills the guards, throws the gun at you, and blames you for the incident.")
            time.sleep(2)
            dialog("Guards run in and separate you two. They watch the camera footage, witnessing the general's treason.")
            dialog("Guards: For the crime of murder and treason, you are under arrest.")
            dialog("General: Oh, am I now?")
            dialog("General: I guess this country has nothing to offer me now.")
            dialog("The general presses a button, and the whole fort goes kaboom.")
        else:
            dialog("The General kills the guards, throws the gun at you, and blames you for the incident.")
            dialog("Guards run in and separate you two. They watch the camera footage, witnessing the general's treason.")
            dialog("Guards: For the crime of murder and treason, you are under arrest.")
            dialog("General: Oh, am I now?")
            dialog("General: I guess this country has nothing to offer me now.")
            dialog("The general presses a button, and the whole fort goes kaboom.")
    else:
        dialog("The General kills the guards, throws the gun at you, and blames you for the incident.")
        dialog("Guards run in and separate you two. They watch the camera footage, witnessing the general's treason.")
        dialog("Guards: For the crime of murder and treason, you are under arrest.")
        dialog("General: Oh, am I now?")
        dialog("General: I guess this country has nothing to offer me now.")
        dialog("The general presses a button, and the whole fort goes kaboom.")

dialog("General: Sit down.")
time.sleep(2)
dialog("You sit down.")
time.sleep(2)
arrest_player()

import time

class Game:
    def __init__(self):
        self.health = 5000
        self.armor = 2000
        self.damage = 4000

    def play(self):
        print("You wake up in the rubble of the building, armed with a 1911 pistol.")
        print("A Wadiyan soldier charges at you.")
        self.shoot_enemy()
        self.find_tools()

    def shoot_enemy(self):
        print("You shoot the Wadiyan soldier and eliminate the immediate threat.")

    def find_tools(self):
        print("You find a map with crucial information, but the Apache helicopter attacks.")
        self.dodge_apache()
        print("You make it to the armory and obtain an EMP device.")
        self.dodge_apache()
        print("You then head to the range and acquire an IGLA manpads launcher.")
        self.dodge_apache()
        print("You successfully disable the Apache with the EMP device.")
        print("You lock on and shoot down the Apache with the IGLA launcher.")

    def dodge_apache(self):
        print("The Apache helicopter attacks! Type 'd' to dodge!")
        while True:
            user_input = input("> ")
            if user_input.lower() == "d":
                print("You successfully dodge the attack!")
                time.sleep(3)  # Wait for next attack
            else:
                print("You failed to dodge the attack. You are killed by the Apache.")
                break



    def fight_general(self):
        print("You wake up to find the General approaching. He stabs you with a knife.")
        self.defend_yourself()

    def defend_yourself(self):
        print("Ruslan arrives and punches the General. You try to crawl and pick up a Magnum.")
        self.attack_general()

    def attack_general(self):
        print("You take out the knife from your chest.")
        print("Suddenly, the General kicks Ruslan and starts punching him.")
        self.throw_knife()

    def throw_knife(self):
        print("You aim at the General's head and throw the knife.")
        print("The knife hits the General in the eye, and he dies.")
        self.rescue_ruslan()

    def rescue_ruslan(self):
        print("An injured Ruslan calls for immediate extraction.")
        print("You both make it to an MI-8 helicopter.")
        print("However, your injuries prove fatal, and you succumb to them.")
        self.game_over()

    def game_over(self):
        print("THE END!")

# Start the game
game = Game()
game.play()
game.fight_general()


