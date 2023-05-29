class Juggernaut:
    def __init__(self):
        self.weapon = "Minigun"
        self.damage = 100
        self.ammo = 200
        self.reload_time = 20
        self.health = 500
        self.armor = 500

    def description(self):
        print("An armored behemoth, with more ammo to go around than there are people to kill.")

class Paratrooper:
    def __init__(self):
        self.weapon = "M4A1"
        self.damage = 50
        self.ammo = 30
        self.reload_time = 3
        self.health = 600
        self.armor = 200

    def description(self):
        print("A special operator, who moves unseen and lives up to his reputation as elite.")

class DemolitionMan:
    def __init__(self):
        self.weapon = "MGL-32 Grenade Launcher"
        self.damage = 500
        self.ammo = 6
        self.reload_time = 12
        self.health = 100
        self.armor = 300

    def description(self):
        print("A man trained in the art of explosives who knows how to make things go boom.")

class Killstreak:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def description(self):
        print(self.name + ":")
        print("Health:", self.health)
        print("Armor:", self.armor)
        print("Damage:", self.damage)

killstreaks = [
    Killstreak("MI-24 helicopter", 1000, 5000, 4000),
    Killstreak("AC-130 gunship", 2000, 4000, 5000),
    Killstreak("Tu-160", 3000, 3000, 6000),
    Killstreak("Yak-141 VTOL jet", 500, 2000, 5000),
    Killstreak("Su-25", 4000, 6000, 2000)
]

def select_class():
    print("You are a soldier in the United States Army Rangers, and you have been sent to fight in the Republic of Wadiya.")
    print("You arrive at Fort Ripton, a military base in the occupied province of Al Hilal, and at sunrise are immediately called to the armory to select your choice of gear by high command.")
    print("In the armory, you see 3 gear choices:")
    print("1. Juggernaut")
    print("2. Paratrooper")
    print("3. Demolition Man")

    choice = int(input("Enter the number of your chosen class: "))

    if choice == 1:
        player_class = Juggernaut()
    elif choice == 2:
        player_class = Paratrooper()
    elif choice == 3:
        player_class = DemolitionMan()
    else:
        print("Invalid choice. Please select a valid class.")
        return select_class()

    print("You have chosen the", player_class.__class__.__name__)
    player_class.description()
    return player_class

def use_buy_station(points):
    print("You come across an NPC who instructs you on how to use a buy station.")
    print("You currently have", points, "points.")

    print("The following killstreaks are available for purchase:")
    for i, killstreak in enumerate(killstreaks):
        print(i+1, "-", killstreak.name)

    choice = int(input("Enter the number of the killstreak you want to purchase: "))

    if choice < 1 or choice > len(killstreaks):
        print("Invalid choice. Please select a valid killstreak.")
        return use_buy_station(points)

    selected_killstreak = killstreaks[choice - 1]
    if points >= 2000:
        print("You have purchased the", selected_killstreak.name)
        selected_killstreak.description()
        points -= 2000
    else:
        print("You don't have enough points to purchase this killstreak.")

    return points

def encounter_enemies(points, health):
    print("\nYou come across 10 enemies guarding the gate.")

    print("What do you want to do?")
    print("1. Call in a drone strike")
    print("2. Engage the enemies with your gun")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You call in a drone strike. All enemies are eliminated.")
        points += 20 * 10
    elif choice == 2:
        print("You engage the enemies with your gun.")

        for _ in range(10):
            health -= 300
            points += 20

        print("You eliminate all enemies, but take damage in the process.")

    return points, health

def choose_path(points, health):
    print("\nAfter dealing with the enemies, you have a choice:")
    print("1. Climb the air traffic control tower")
    print("2. Move through the buildings")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("As you climb the air traffic control tower, it gets hit by RPG fire.")
        print("You take 200 damage.")
        health -= 200
    elif choice == 2:
        print("While moving through the buildings, you step on a claymore.")
        print("You take 150 damage.")
        health -= 150

    return points, health

def engage_final_encounter(points, health):
    print("\nYou reach the runway, where the final encounter takes place.")

    print("What do you want to do?")
    print("1. Wait for your team and engage together")
    print("2. Engage by yourself")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You wait for your team to catch up and engage together.")
        print("You successfully eliminate all enemies.")
    elif choice == 2:
        print("You decide to engage the enemies by yourself.")
        print("You take 70 damage, but manage to eliminate all enemies.")

        health -= 70

    return points, health

def game():
    player = select_class()
    points = 2000
    health = player.health

    print("\n--- GAME START ---")
    print("You are now on a mission to secure a heavily armed Wadiyan objective.")
    print("The objective is a fortified compound in the middle of Al Hilal.")
    print("It is a major strategic point that must be captured.")

    print("You start driving and come across an NPC who instructs you on how to use a buy station.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Interact with the buy station")
        print("2. Continue the mission")
        print("3. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            points = use_buy_station(points)
        elif choice == 2:
            points, health = encounter_enemies(points, health)
            points, health = choose_path(points, health)
            points, health = engage_final_encounter(points, health)
            break
        elif choice == 3:
            print("You quit the game.")
            return

    print("\n--- GAME OVER ---")
    print("Points:", points)
    print("Health:", health)

game()


import time

class Killstreak:
    def __init__(self, health, armor, damage):
        self.health = health
        self.armor = armor
        self.damage = damage

def engage_tanks(points):
    tanks = 20
    destroyed_tanks = 0

    print("\nPrivate Andrew Stevens warns you of 20 T-14 Armata tanks heading your way.")

    choice = input("Type 'A' to activate the killstreak: ")

    if choice != "A":
        print("Invalid input. The tanks overpower you.")
        return points

    killstreak = Killstreak(1000, 4000, 300)

    print("Engaging the tanks with the killstreak.")

    while destroyed_tanks < tanks:
        print("\nWhat do you want to do?")
        print("1. Type 'fire' to attack the tanks")
        print("2. Wait for the tanks to attack")

        choice = input("Enter your choice: ")

        if choice == "fire":
            tank_index = destroyed_tanks
            if tank_index >= tanks:
                print("No more tanks to destroy.")
                break

            tank = tanks[tank_index]
            tank.health -= killstreak.damage

            if tank.health <= 0:
                print("Tank destroyed!")
                points += 100
                destroyed_tanks += 1
        else:
            print("The tanks continue to advance.")

        time.sleep(5)

        killstreak.health -= 300

        if killstreak.health <= 0:
            print("Your killstreak is destroyed. The tanks overpower you.")
            return points

    print("All tanks destroyed. Mission accomplished!")

    return points

def return_to_base():
    print("\nYour killstreak flies away and the mission ends.")
    print("You return back to base.")

def game():
    points = 2000

    print("You are a soldier in the United States Army Rangers.")
    print("You have been sent to fight in the Republic of Wadiya.")

    # Rest of the game code

    points = engage_tanks(points)
    return_to_base()

game()

import time

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

def game():
    points = 2000

    print("You are a soldier in the United States Army Rangers.")
    print("You have been sent to fight in the Republic of Wadiya.")

    points = defend_wave(25, 0, points)
    points = interact_with_buystation(points)
    points = defend_wave(50, 10, points)
    exfil()

game()

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
            print("General Karim: 'Since you failed to provide the correct answer, an innocent man must pay the price.'")
            print("The general hits you with a revolver, and you witness the death of another man.")

        print("General Karim: 'Now, tell me, who stole the key to the prison armory?'")

        answer_2 = input("A) It was Ruslan\n"
                         "B) It was the guard who misplaced it\n"
                         "C) I will not tell you\n"
                         "Enter your choice (A, B, or C): ")

        if answer_2 == "A" or answer_2 == "B":
            print("General Karim: 'You are responsible for the lives that are lost.'")
            print("The general hits you with a revolver, and another innocent man loses his life.")
        else:
            print("General Karim: 'Your defiance will have consequences.'")
            print("The general puts you into a chokehold, but suddenly an explosion rocks the building.")
            print("General Karim is forced to release you and flee the scene.")

def prison_escape():
    print("After the explosion, chaos ensues in the prison. The opportunity for escape arises.")

    # Add logic for the prison escape scenario

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

    # Add logic to handle combat with enemies using chosen weapon or grenade

    print("After dealing with the enemies, you enter another room and are attacked by a Wadiyan Soldier.")

    # Add logic for the encounter with the Wadiyan Soldier

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

# Start the game
game = Game()
game.play()

class Game:
    # ... existing code ...

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


