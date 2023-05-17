class ApacheHelicopter:
    def __init__(self):
        self.health = 3000
        self.armor = 2000
        self.damage = 4000
        self.speed = 100

    def attack(self):
        print("Apache helicopter is attacking with {} damage.".format(self.damage))

    def move(self):
        print("Apache helicopter is moving at a speed of {}.".format(self.speed))

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
            print("Apache helicopter has been destroyed.")

    def is_alive(self):
        return self.health > 0