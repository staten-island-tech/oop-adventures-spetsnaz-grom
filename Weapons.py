class M4A1:
    def __init__(self):
        self.range = 300
        self.damage = 50
        self.magazine_capacity = 30
        self.ammo_count = self.magazine_capacity

    def shoot(self, distance):
        if distance <= self.range:
            if self.ammo_count > 0:
                self.ammo_count -= 1
                print("M4A1 rifle fires and deals {} damage.".format(self.damage))
            else:
                print("M4A1 rifle is out of ammo. Reload!")
        else:
            print("Target is beyond the effective range of the M4A1 rifle.")

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





class Pistol1911:
    def __init__(self):
        self.range = 50
        self.ammo_capacity = 7
        self.damage = 30

    def shoot(self):
        if self.ammo_capacity > 0:
            print("1911 pistol shoots with {} damage.".format(self.damage))
            self.ammo_capacity -= 1
        else:
            print("1911 pistol is out of ammo. Reload!")

    def reload(self):
        print("Reloading 1911 pistol.")
        self.ammo_capacity = 7