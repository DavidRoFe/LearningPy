class Wizard():
    
    mana =  100
    def __init__(self, name, power):

        self.name  = name
        self.power = power

    def attack(self):

        self.mana -= 10
        return (f'Attacking with the power of {self.power}')
    
    def check_mana(self):

        return (f'{self.mana} remaining')

class Archer():

    def __init__(self, name, arrows):

        self.name = name
        self.arrows = arrows
    
    def attack(self):

        self.arrows -= 1
        return (f'Attacking with one arrow')

    def check_arrows(self):

        return (f'{self.arrows} remaining')

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

print(player_00.attack(bow=True, magic=False))
print(player_00.attack(bow=False, magic=True))

print(player_00.check_mana())
print(player_00.check_arrows())