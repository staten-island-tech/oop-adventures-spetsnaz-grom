class Gunship:
    def __init__(self):
        self.health = 4000
        self.armor = 7000
        self.damage = 7000
        self.speed = 50

    def attack(self):
        print("Gunship(name) is attacking with {} damage.".format(self.damage))

    def move(self):
        print("Gunship(name) is moving at a speed of {}.".format(self.speed))

    def take_damage(self, amount):
        if self.armor > 0:
            if self.armor >= amount:
                self.armor -= amount
            else:
                remaining_damage = amount - self.armor
                self.armor = 0
                self.health -= remaining_damage
        else:
            self.health -= amount

        if self.health <= 0:
            self.health = 0
            print("Gunship(name) has been destroyed.")

    def is_alive(self):
        return self.health > 0