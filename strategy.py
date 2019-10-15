class Creature():
    choice = None
    def __init__(self, name):
        self.name = name
    def movement_method(self, choice):
        self.choice = choice
    def info(self):
        print(f'movement method = {self.choice.go()}')

class types_of_movement():
    def go(self):
        return 'no strategy in here'
class using_only_legs(types_of_movement):
    def go(self):
        return 'I can walk'
class using_extremities(types_of_movement):
    def go(self):
        return "i can't walk using only legs or hands or even i don't have hands"

class Animal(Creature):
    choice = using_extremities()

class Human(Creature):
    choice = using_only_legs()

Pchelovek = Human('Denis')
Kaban = Animal('Baran')
Pchelovek.info()