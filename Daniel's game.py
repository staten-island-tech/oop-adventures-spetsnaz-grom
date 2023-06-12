class Juggernaut:
    def __init__(self):
        self.weapon = "Minigun"
        self.damage = 100
        self.ammo = 200
        self.reload_time = 20
        self.health = 500
        self.armor = 500

    def description(self):
        return "An armored behemoth, with more ammo to go around than there are people to kill."


class Paratrooper:
    def __init__(self):
        self.weapon = "M4A1"
        self.damage = 50
        self.ammo = 30
        self.reload_time = 3
        self.health = 600
        self.armor = 200

    def description(self):
        return "A special operator, who moves unseen and lives up to his reputation as elite."


class DemolitionMan:
    def __init__(self):
        self.weapon = "MGL-32 Grenade Launcher"
        self.damage = 500
        self.ammo = 6
        self.reload_time = 12
        self.health = 100
        self.armor = 300

    def description(self):
        return "A man trained in the art of explosives who knows how to make things go boom."


class Killstreak:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def description(self):
        descriptions = {
            "AC-130": "The vehicle version of the doom slayer",
            "MI-24": "Nicknamed the Devil's chariot or the Flying tank, the fearsome Mi-24 lives up to its reputation as one nasty warbird",
            "Tu-160": "An unstoppable force with firepower capable of destroying everything in its path",
            "Yak-141": "A mean machine capable of dominating the skies",
            "Su-25": "Brrrrrrt"
        }
        return descriptions.get(self.name, "Unknown Killstreak")

    def __str__(self):
        return self.name


def select_class():
    print("Welcome to the game!")
    print("You are a soldier in the United States Army Rangers.")
    print("You have been sent to fight in the Republic of Wadiya.")
    print("You arrive at Fort Ripton, a military base in the occupied province of Al Hilal.")
    print("At sunrise, you are immediately called to the armory to select your choice of gear by high command.")
    print("In the armory, you see 3 gear choices:")
    print("1. Juggernaut")
    print("2. Paratrooper")
    print("3. Demolition Man")

    class_choice = input("Enter the number of your desired class: ")

    if class_choice == "1":
        player_class = Juggernaut()
    elif class_choice == "2":
        player_class = Paratrooper()
    elif class_choice == "3":
        player_class = DemolitionMan()
    else:
        print("Invalid input. Please try again.")
        return select_class()

    print("\nYou have selected the", player_class.__class__.__name__)
    print(player_class.description())

    return player_class


def buy_killstreak(player_points):
    killstreaks = [
        Killstreak("AC-130", health=2000, armor=4000, damage=5000),
        Killstreak("MI-24", health=1000, armor=5000, damage=4000),
        Killstreak("Tu-160", health=3000, armor=3000, damage=6000),
        Killstreak("Yak-141", health=500, armor=2000, damage=5000),
        Killstreak("Su-25", health=4000, armor=6000, damage=2000)
    ]

    print("\nYou encounter an NPC who instructs you on how to use the buystation.")
    print("To use the buystation, type 1 to interact.")
    interaction_choice = input("Enter 1 to interact: ")

    if interaction_choice != "1":
        print("You ignore the NPC and continue on your mission.")
        return None

    print("\nYou approach the buystation.")
    print("Available killstreaks:")
    for i, killstreak in enumerate(killstreaks, start=1):
        print(f"{i}. {killstreak.name} (Cost: 2000 points) - {killstreak.description()}")

    killstreak_choice = input("Enter the number of your desired killstreak: ")

    try:
        killstreak_index = int(killstreak_choice) - 1
        selected_killstreak = killstreaks[killstreak_index]
        if player_points >= 2000:
            player_points -= 2000
            print(f"\nYou have purchased the {selected_killstreak.name} killstreak!")
            print(f"Remaining points: {player_points}")
            return selected_killstreak
        else:
            print("Insufficient points to purchase the selected killstreak.")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

    return None


def play_game(player_class, selected_killstreak):
    player_points = 2000
    enemy_count = 10
    player_damage = 0
    total_points = 0
    enemy_health = 300

    print("\nYou have been deployed to secure a heavily armed Wadiyan objective.")
    print("The objective is a fortified compound in the middle of Al Hilal.")
    print("It is a major strategic point that must be captured.")
    print("You arrive at the objective and encounter 10 enemies guarding the gate.")

    while enemy_count > 0:
        print("\nWhat do you want to do?")
        print("1. Call in a drone strike")
        print("2. Engage enemies with your gun")

        action_choice = input("Enter the number of your desired action: ")

        if action_choice == "1":
            print("You call in a drone strike on the base.")
            enemy_count = 0
            total_points += enemy_count * 20
        elif action_choice == "2":
            print("You engage enemies with your gun.")
            player_damage += enemy_count * enemy_health
            total_points += enemy_count * 20
            enemy_count = 0
        else:
            print("Invalid input. Please try again.")

    print("\nYou have secured the objective.")
    print("You have two options for your next move:")
    print("1. Climb the air traffic control tower")
    print("2. Move through the buildings")

    move_choice = input("Enter the number of your desired move: ")

    if move_choice == "1":
        print("You climb the air traffic control tower.")
        print("Suddenly, the tower is hit by RPG fire.")
        player_damage += 200
    elif move_choice == "2":
        print("You move through the buildings.")
        print("Unfortunately, you step on a claymore.")
        player_damage += 150
    else:
        print("Invalid input. Please try again.")

    print("\nYou proceed to the runway.")
    print("You have one final decision to make:")
    print("1. Wait for your team to catch up and engage together")
    print("2. Engage by yourself")

    engagement_choice = input("Enter the number of your desired engagement: ")

    if engagement_choice == "1":
        print("You wait for your team to catch up.")
        print("Together, you engage and eliminate the remaining enemies.")
    elif engagement_choice == "2":
        print("You decide to engage by yourself.")
        player_damage += 70
        print("You take 70 damage but manage to eliminate the remaining enemies.")
    else:
        print("Invalid input. Please try again.")

    player_points -= player_damage
    total_points += player_damage

    print("\nMission complete!")
    print("Points earned:", total_points)
    print("Remaining health points:", player_class.health - player_damage)
    print("Remaining armor points:", player_class.armor - player_damage)
    print("Remaining points:", player_points)


# Main game loop
player_class = select_class()
selected_killstreak = buy_killstreak(player_points=2000)

if player_class and selected_killstreak:
    play_game(player_class, selected_killstreak)
else:
    print("Game over.")

import time

class Tank:
    def __init__(self, armor, health, damage):
        self.armor = armor
        self.health = health
        self.damage = damage

class ArmoredEnemy:
    def __init__(self, armor, health):
        self.armor = armor
        self.health = health

class Player:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor

def engage_tanks(player, tanks, killstreak):
    print("\nPrivate Andrew Stevens warns you of 20 T-14 Armata tanks heading your way.")
    print("You activate your killstreak and engage the tanks.")

    for i, tank in enumerate(tanks, start=1):
        print(f"\nTank {i} - Armor: {tank.armor}, Health: {tank.health}, Damage: {tank.damage}")
        print("Type 'fire' to attack the tank with your killstreak.")

        while True:
            action_choice = input("Enter your action: ")

            if action_choice.lower() == "fire":
                tank_health = tank.health
                killstreak_damage = killstreak.damage

                if killstreak_damage >= tank_health:
                    print("You destroy the tank!")
                    killstreak_damage -= tank_health
                    tank_health = 0
                else:
                    print("You damage the tank!")
                    tank_health -= killstreak_damage
                    killstreak_damage = 0

                tank.health = tank_health
                killstreak.damage = killstreak_damage
                break
            else:
                print("Invalid action. Please try again.")

        if tank_health <= 0:
            print("Tank destroyed!")
            


        time.sleep(5)
        print("One of the tanks launches an anti-air missile at your killstreak!")
        killstreak_damage = 300
        print(f"Your killstreak takes {killstreak_damage} damage.")
        killstreak.health -= killstreak_damage

    print("\nAll tanks destroyed!")
    print("Your killstreak flies away.")

def defend_rooftop(player, enemy_count):
    print("\nYour Humvee gets blown up by RPG fire, and you take shelter on the rooftop of a blown-up building.")
    print("Waves of enemies approach the building.")

    player_health = player.health
    wave = 1

    while enemy_count > 0:
        print(f"\nWave {wave} - Enemies Remaining: {enemy_count}")
        print("You have two options:")
        print("1. Set explosives and prepare an ambush")
        print("2. Attack with an abandoned PKM")

        action_choice = input("Enter your action: ")

        if action_choice == "1":
            print("You set explosives and prepare for an ambush.")
            print("The enemies approach and get caught in the explosion.")
            enemy_count -= min(enemy_count, 25)
        elif action_choice == "2":
            pkm_damage = 200
            pkm_ammo = 200
            reload_time = 5
            enemy_damage = 200

            print("You pick up the abandoned PKM and start firing.")
            print("Press 'F' to fire the PKM.")

            while pkm_ammo > 0 and enemy_count > 0:
                action_choice = input("Press 'F' to fire: ")

                if action_choice.lower() == "f":
                    pkm_ammo -= 1
                    enemy_count -= 1
                    player_health -= enemy_damage

                    print(f"You fire the PKM and take down an enemy. PKM Ammo: {pkm_ammo}, Enemies Remaining: {enemy_count}")

                    if player_health <= 0:
                        print("You were shot and killed by an enemy!")
                        break

                time.sleep(reload_time)

            if enemy_count <= 0:
                print("You have eliminated all enemies.")
            else:
                print("You have run out of PKM ammo.")

        wave += 1

def interrogation(player):
    print("\nA CH-53 arrives to exfil you.")
    print("You board the helicopter and leave the area.")
    print("Unfortunately for you a wadiyan S-300 missile system takes aim at your chopper, and shoots it down along with you.")
    print("Your entire team dies, and you fall out of the burning heli cargo hold.")
    print ("A Wadiyan patrol finds your crash site and take you back to the camp.")
    print ("You spend 8 months in the camps prison complex which is quite large.")
    print ("You meet a Russian Spetsnaz Gru operator named Ruslan Pelishkov who was captured by the Wadiyans.")
    print ("You and Ruslan become close friends, and soon he entrusted to you a key.")
    print ("Ruslan also gives you a long range radio device, that you use to talk to Russian forces, since officially Ruslan was denounced by his country")
    print ("An bombing raid by a Tu-160 hits the camps headquarters, and you are suspected of carrying it out")
    print ("You are knocked out and are tooken somewhere.")

player = Player(1000, 0)
tanks = [Tank(4000, 1000, 300) for _ in range(20)]
armored_enemies = [ArmoredEnemy(300, 600) for _ in range(10)]

engage_tanks(player, tanks, selected_killstreak)

if player.health > 0:
    defend_rooftop(player, 50)

import time
import random

class Player:
    def __init__(self, health, ammo):
        self.health = health
        self.ammo = ammo

class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

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
    print("With the help of a giant explosion, chaos ensues in the prison. The opportunity for escape arises, and you escape.")

    weapon_choice = None

    while weapon_choice not in ["AK-47", "SVD-63"]:
        print("\nChoose a weapon to wield:")
        print("1) AK-47 - 30 rounds, 60 damage, reload time: 3 seconds")
        print("2) SVD-63 - 10 rounds, 120 damage, reload time: 5 seconds")

        weapon_choice = input("Enter your choice: ")

        if weapon_choice == "1":
            player.ammo = 30
        elif weapon_choice == "2":
            player.ammo = 10

    print("You pick up the", weapon_choice)

    print("\nYou navigate through the prison, encountering enemies along the way.")

    enemy_count = 6
    enemy_damage = 200
    grenade_damage = 500
    grenade_count = 2

    while enemy_count > 0:
        print(f"\nEnemies Remaining: {enemy_count}")
        print("Choose your action:")
        print("1) Shoot with your weapon")
        print("2) Throw a grenade")

        action_choice = input("Enter your action: ")

        if action_choice == "1":
            if player.ammo > 0:
                player.ammo -= 1
                enemy_count -= 1
                print("You shoot an enemy.")
            else:
                print("You are out of ammo.")

            time.sleep(3)
            print("One of the enemies fires at you!")
            player.health -= enemy_damage

        elif action_choice == "2":
            if grenade_count > 0:
                grenade_count -= 1
                enemy_count -= 1
                print("You throw a grenade and eliminate an enemy.")
            else:
                print("You are out of grenades.")

            time.sleep(3)
            print("One of the enemies fires at you!")
            player.health -= enemy_damage

        if player.health <= 0:
            print("You were shot and killed by an enemy!")
            break

    if player.health > 0:
        print("\nYou enter another room but get attacked by a Wadiyan soldier.")
        print("Before he can shoot you, he is shot by Spetsnaz GRU team members who have come to rescue you.")

player = Player(300, 0)
interrogation(player)


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

        print("You see the General sprinting away to a Wadiyan UH-1")
        print ("With your last rocket you take aim on the helicopter high above your head, and you fire")
        print ("A piece of the helicopter hits you on your head and you get knocked out")
    
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