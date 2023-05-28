class BuyStation:
    def __init__(self, player):
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
        self.player = player
        self.purchased_items = []

    def display_menu(self):
        print("Buy Station Menu:")
        for choice, item in self.choices.items():
            print("{}: {}".format(choice, item))

    def interact(self):
        choice = input("Press B to interact with the Buy Station: ")
        if choice.upper() == 'B':
            self.display_menu()
            self.buy()

    def buy(self):
        choice = input("Press A to buy a choice: ")
        if choice.upper() == 'A':
            item = input("Enter the number of the item you want to buy: ")
            if item in self.choices:
                selected_item = self.choices[item]
                cost = self.item_costs[selected_item]
                if self.player.points >= cost:
                    print("You bought: {}".format(selected_item))
                    self.player.points -= cost
                    print("Points remaining: {}".format(self.player.points))
                    self.purchased_items.append(selected_item)
                else:
                    print("Insufficient points to buy the item.")
            else:
                print("Invalid choice. Please try again.")

    def process_purchase(self, item):
        pass


class Killstreak:
    def __init__(self):
        self.available_killstreaks = {
            'AC-130 gunship': AC130Gunship(),
            'MI-24 helicopter': MI24Helicopter(),
            'Tu-95 bomber run': TU95Bomber(),
            'Yak-38 VTOL jet': Yak38VTOL(),
            'BTR-90 APC': BTR90APC()
        }

    def deploy_killstreak(self, item):
        if item in self.available_killstreaks:
            killstreak = self.available_killstreaks[item]
            print("Deploying {} killstreak...".format(item))
            killstreak.attack()
            # Handle the killstreak logic here, such as damaging enemies or providing support to the player
        else:
            print("Invalid killstreak item. Please try again.")


class Player:
    def __init__(self):
        self.points = 2000


class AC130Gunship:
    # AC-130Gunship class code...

class MI24Helicopter:
    # MI24Helicopter class code...

class BTR90APC:
    # BTR90APC class code...

class TU95Bomber:
    # TU95Bomber class code...

class Yak38VTOL:
    # Yak38VTOL class code...


# Main game logic
player = Player()
buy_station = BuyStation(player)
killstreak = Killstreak()

while True:
    # Game loop
    print("Game loop...")
    # Perform game actions and update player's points

    # Interact with Buy Station
    buy_station.interact()

    # Check if player wants to deploy purchased killstreaks
    if buy_station.purchased_items:
        deploy_choice = input("Press D to deploy a purchased killstreak: ")
        if deploy_choice.upper() == 'D':
            item = input("Enter the number of the purchased killstreak to deploy: ")
            if item in buy_station.purchased_items:
                buy_station.purchased_items.remove(item)
                killstreak.deploy_killstreak(item)
            else:
                print("Invalid killstreak item. Please try again.")
