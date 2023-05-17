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
        self.points = 0

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
                if self.points >= cost:
                    print("You bought: {}".format(selected_item))
                    self.points -= cost
                    self.process_purchase(selected_item)
                else:
                    print("Insufficient points to buy the item.")
            else:
                print("Invalid choice. Please try again.")

    def process_purchase(self, item):
        # Add code here to handle the logic of the purchased item
        pass
