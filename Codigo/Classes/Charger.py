class Charger:
    def __init__(self):
        print("Charger class initialized!")
        self.turn_off_charger()
        self.charger_state = False

    def turn_on_charger(self):
        print("Charger turned on")
        self.charger_state = True

    def turn_off_charger(self):
        print("Charger turned off")
        self.charger_state = False

    def check_charger_state(self):
        if (self.charger_state == True):
            print("Charger state is on")
        else:
            print("Charger state is off")

