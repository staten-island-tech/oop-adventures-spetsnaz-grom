import random
import time

# Tower Class
class Tower:
    def __init__(self, name, cost, base_damage, max_level, upgrade_damage, final_form):
        self.name = name
        self.cost = cost
        self.base_damage = base_damage
        self.max_level = max_level
        self.upgrade_damage = upgrade_damage
        self.final_form = final_form
        self.level = 1

    def upgrade(self):
        if self.level < self.max_level:
            self.level += 1

    def get_damage(self):
        if self.level < self.max_level:
            return self.base_damage + (self.level - 1) * self.upgrade_damage
        else:
            return self.final_form

    def get_cost(self):
        return self.cost


# Enemy Class
class Enemy:
    def __init__(self, name, health, points):
        self.name = name
        self.health = health
        self.points = points

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0


# Game Class
class TowerDefenseGame:
    def __init__(self):
        self.towers = [
            Tower("Mi-4", 2000, 40, 4, 40, 200),
            Tower("Il-40", 4000, 50, 4, 50, 400),
            Tower("A-26", 3000, 10, 4, 10, 450),
            Tower("UH-1", 10, 30, 4, 30, 250),
            Tower("Infantry", 100, 5, 4, 5, 100),
            Tower("Spetsnaz", 500, 15, 4, 15, 180),
            Tower("T-34", 7000, 100, 4, 100, 300),
            Tower("BM-13", 70, 70, 4, 70, 500)
        ]
        self.enemies = [
            Enemy("Zombie", 10, 10),
            Enemy("Armored Zombie", 100, 100),
            Enemy("Panzersoldat", 300, 300),
            Enemy("Zombified Tank", 1000, 1000),
            Enemy("Uranium Man", 5000, 5000)
        ]
        self.bunker_health = 300
        self.round = 1
        self.xp = 0

    def start_game(self):
        print("Tower Defense Game - Let's defend the bunker!")

        while self.bunker_health > 0:
            print(f"\n--- Round {self.round} ---")
            self.spawn_enemies()
            self.take_turn()

            if self.round == 41:
                self.boss_fight()
                break

            self.round += 1
            self.xp += 300
            self.upgrade_towers()

        print("\nYou have lost the game! The bunker has been destroyed.")

    def spawn_enemies(self):
        if self.round <= 10:
            num_zombies = 10 + (self.round - 1) * 5
            for _ in range(num_zombies):
                enemy = random.choice(self.enemies[:1])
                self.attack_bunker(enemy)
        elif self.round <= 20:
            num_zombies = 10 + (self.round - 11) * 5
            num_armored_zombies = num_zombies
            for _ in range(num_zombies):
                enemy = random.choice(self.enemies[:2])
                self.attack_bunker(enemy)
            for _ in range(num_armored_zombies):
                enemy = random.choice(self.enemies[:1])
                self.attack_bunker(enemy)
        elif self.round <= 30:
            num_zombies = 10 + (self.round - 21) * 5
            num_armored_zombies = num_zombies
            num_panzersoldats = num_zombies
            for _ in range(num_zombies):
                enemy = random.choice(self.enemies[:3])
                self.attack_bunker(enemy)
            for _ in range(num_armored_zombies):
                enemy = random.choice(self.enemies[:2])
                self.attack_bunker(enemy)
            for _ in range(num_panzersoldats):
                enemy = random.choice(self.enemies[:3])
                self.attack_bunker(enemy)
        else:
            num_zombies = 10 + (self.round - 31) * 5
            num_armored_zombies = num_zombies
            num_panzersoldats = num_zombies
            num_ztanks = num_zombies
            for _ in range(num_zombies):
                enemy = random.choice(self.enemies[:4])
                self.attack_bunker(enemy)
            for _ in range(num_armored_zombies):
                enemy = random.choice(self.enemies[:2])
                self.attack_bunker(enemy)
            for _ in range(num_panzersoldats):
                enemy = random.choice(self.enemies[:3])
                self.attack_bunker(enemy)
            for _ in range(num_ztanks):
                enemy = random.choice(self.enemies[:4])
                self.attack_bunker(enemy)

    def attack_bunker(self, enemy):
        while enemy.health > 0 and self.bunker_health > 0:
            damage = random.randint(1, 10)
            enemy.take_damage(damage)
            self.bunker_health -= 10

            if self.bunker_health <= 0:
                break

            print(f"{enemy.name} attacked the bunker for {damage} damage.")
            print(f"Bunker health: {self.bunker_health}\n")

            time.sleep(0.5)

    def take_turn(self):
        print("Towers are attacking the enemies.")

        for tower in self.towers:
            damage = tower.get_damage()
            enemy = random.choice(self.enemies)
            enemy.take_damage(damage)

            print(f"{tower.name} dealt {damage} damage to {enemy.name}.")

            if enemy.is_dead():
                self.xp += enemy.points
                print(f"{enemy.name} has been defeated. +{enemy.points} XP!\n")
                self.enemies.remove(enemy)

            time.sleep(0.5)

    def upgrade_towers(self):
        for tower in self.towers:
            if self.xp >= tower.get_cost():
                self.xp -= tower.get_cost()
                tower.upgrade()
                print(f"{tower.name} has been upgraded to level {tower.level}.")

    def boss_fight(self):
        uranium_man = Enemy("Uranium Man", 5000, 5000)

        while uranium_man.health > 0 and self.bunker_health > 0:
            self.attack_bunker(uranium_man)

        if self.bunker_health > 0:
            print("\n--- Uranium Man defeated! ---")
            print("Uranium Man splits into two halves, Thrasher and Brawler.")

            thrasher = Enemy("Thrasher", 2500, 2500)
            brawler = Enemy("Brawler", 2500, 2500)

            while thrasher.health > 0 and brawler.health > 0 and self.bunker_health > 0:
                self.attack_bunker(thrasher)
                self.attack_bunker(brawler)

            if self.bunker_health > 0:
                print("\n--- You have prevailed! ---")
                print("Congratulations! You have successfully defended the bunker.")

    def print_stats(self):
        print(f"Bunker health: {self.bunker_health}")
        print(f"Round: {self.round}")
        print(f"XP: {self.xp}")

# Start the game
game = TowerDefenseGame()
game.start_game()
