class Wizard():
    
    mana =  100
    def __init__(self, name, power):

        self.name  = name
        self.power = power

    def attack(self):

        print(f'Attacking with the power of {self.power}')
        self.mana -= 10
    
    def check_mana(self):

        print(f'{self.mana} remaining')

class Archer():

    def __init__(self, name, arrows):

        self.name = name
        self.arrows = arrows
    
    def attack(self):

        print(f'Attacking with one arrow')
        self.arrows -= 1

    def check_arrows(self):

        print(f'{self.arrows} remaining')

class Hybrid(Wizard, Archer):

    def __init__(self, name, power, arrows):

        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

    def attack(self, magic, bow):
        
        if magic:

            Wizard.attack(self)


        elif bow:

            Archer.attack(self)


player_00 = Hybrid('Pepe', 50, 100)

player_00.attack(bow=True, magic=False)
player_00.attack(bow=False, magic=True)

player_00.check_mana()
player_00.check_arrows()