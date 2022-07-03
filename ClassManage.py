# Class definition
from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
from tkinter.messagebox import NO, YES


class PlayerCharacter:
    # Attributes
    specie = 'Human'
    legal_age = 18

    def __init__(self, name, age, gender, runing=False):

        if age < PlayerCharacter.legal_age:

            print(
                f'{name}, you are too young to play this game, get older and come back!')

        self.name = name
        self.age = age
        self.gender = gender
        self.runing = runing
    # End __init__

    def run(self):

        self.runing = True
        return('runing now!')
    # End run

    def walk(self):

        self.runing = False
        return('walking now!')
    # End walk

    def doChangeSpeed(self):

        if self.runing == False:

            if input(f'{self.name}, do you want to run? ') == YES:

                print(f'{self.name} is {self.run()}')

            else:

                print(f'{self.name} is {self.walk()}')

        else:

            if input(f'{self.name}, do you want to stop runing? ') == YES:

                print(f'{self.name} is {self.walk()}')

            else:

                print(f'{self.name} is {self.run()}')
    # End changeSpeed
# End PlayerCharacter


# Main program
pc_00 = PlayerCharacter(input('What is your name: '),
                        int(input('What is your age: ')),
                        input('What is your gender: '))

if (pc_00.age >= PlayerCharacter.legal_age):

    print(f'{pc_00.name} is {pc_00.age} and he is a {pc_00.gender}')

    pc_00.doChangeSpeed()

    if input(f'{pc_00.name}, do you have a mate? ') == YES:

        pc_01 = PlayerCharacter(input('What is your mate name: '),
                                int(input('What is your mate age: ')),
                                input('What is your mate gender: '))

        if pc_01.age >= PlayerCharacter.legal_age:

            pc_01.doChangeSpeed()

    else:

        pass
