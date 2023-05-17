class MI24Helicopter:
    def __init__(self):
        self.health = 5000
        self.armor = 3000
        self.damage = 4000
        self.speed = 200

    def attack(self):
        print("MI-24 helicopter is attacking with {} damage.".format(self.damage))

    def move(self):
        print("MI-24 helicopter is moving at a speed of {}.".format(self.speed))

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
            print("MI-24 helicopter has been destroyed.")

    def display_description(self):
        print("MI-24 Helicopter Description:")
        print("Nicknamed the Devil's chariot by foreigners or the Flying tank by the Soviet troops, this helicopter packs a punch.")
        print("Health: {}".format(self.health))
        print("Armor: {}".format(self.armor))
        print("Damage: {}".format(self.damage))
        print("Speed: {}".format(self.speed))

# Creating an instance of MI24Helicopter
mi24 = MI24Helicopter()

# Accessing and using its methods
mi24.display_description()
mi24.move()
mi24.attack()
mi24.take_damage(2000)
mi24.take_damage(4000)
mi24.display_description()







class AC130Gunship:
    def __init__(self):
        self.health = 500
        self.armor = 100
        self.damage = 20000
        self.speed = 500

    def attack(self):
        print("AC-130 gunship is attacking with {} damage.".format(self.damage))

    def move(self):
        print("AC-130 gunship is moving at a speed of {}.".format(self.speed))

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
            print("AC-130 gunship has been destroyed.")

    def display_description(self):
        print("AC-130 Gunship Description:")
        print("The ground is the last thing any infantryman or tank crew sees before getting annihilated by the AC-130.")
        print("Health: {}".format(self.health))
        print("Armor: {}".format(self.armor))
        print("Damage: {}".format(self.damage))
        print("Speed: {}".format(self.speed))

# Creating an instance of AC130Gunship
ac130 = AC130Gunship()

# Accessing and using its methods
ac130.display_description()
ac130.move()
ac130.attack()
ac130.take_damage(50)
ac130.take_damage(600)
ac130.display_description()











class BTR90APC:
    def __init__(self):
        self.health = 5000
        self.armor = 400
        self.damage = 500
        self.speed = 100

    def attack(self):
        print("BTR-90 APC is attacking with {} damage.".format(self.damage))

    def move(self):
        print("BTR-90 APC is moving at a speed of {}.".format(self.speed))

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
            print("BTR-90 APC has been destroyed.")

    def display_description(self):
        print("BTR-90 APC Description:")
        print("Made to quickly transport troops, the BTR-90 will get you to and from heavily armed combat zones without any major problems.")
        print("Health: {}".format(self.health))
        print("Armor: {}".format(self.armor))
        print("Damage: {}".format(self.damage))
        print("Speed: {}".format(self.speed))


# Creating an instance of BTR90APC
btr90 = BTR90APC()

# Accessing and using its methods
btr90.display_description()
btr90.move()
btr90.attack()
btr90.take_damage(200)
btr90.take_damage(4000)
btr90.display_description()




class TU95Bomber:
    def __init__(self):
        self.health = 100
        self.armor = 0
        self.damage = 30000000000
        self.speed = 300

    def attack(self):
        print("TU-95 bomber is attacking with {} damage.".format(self.damage))

    def move(self):
        print("TU-95 bomber is moving at a speed of {}.".format(self.speed))

    def take_damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.health = 0
            print("TU-95 bomber has been destroyed.")

    def display_description(self):
        print("TU-95 Bomber Description:")
        print("High altitude bomber capable of turning a beautiful city into an empty crater.")
        print("Health: {}".format(self.health))
        print("Armor: {}".format(self.armor))
        print("Damage: {}".format(self.damage))
        print("Speed: {}".format(self.speed))


# Creating an instance of TU95Bomber
tu95 = TU95Bomber()

# Accessing and using its methods
tu95.display_description()
tu95.move()
tu95.attack()
tu95.take_damage(50)
tu95.take_damage(200)
tu95.display_description()



class Yak38VTOL:
    def __init__(self):
        self.health = 10000
        self.armor = 100
        self.damage = 1000
        self.speed = 1000

    def attack(self):
        print("Yak-38 VTOL jet is attacking with {} damage.".format(self.damage))

    def move(self):
        print("Yak-38 VTOL jet is moving at a speed of {}.".format(self.speed))

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
            print("Yak-38 VTOL jet has been destroyed.")

    def display_description(self):
        print("Yak-38 VTOL Jet Description:")
        print("It's a plane, it's a helicopter, no it's both and you should run.")
        print("Health: {}".format(self.health))
        print("Armor: {}".format(self.armor))
        print("Damage: {}".format(self.damage))
        print("Speed: {}".format(self.speed))


# Creating an instance of Yak38VTOL
yak38 = Yak38VTOL()

# Accessing and using its methods
yak38.display_description()
yak38.move()
yak38.attack()
yak38.take_damage(200)
yak38.take_damage(8000)
yak38.display_description()
