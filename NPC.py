from Person import Person
import random as rnd

class NPC(Person):
    def __init__(self, name) -> None:
        damage = rnd.uniform(0, 100)
        shield = rnd.uniform(0, 0.15)
        super().__init__(name, 100, damage, shield, 1)

    def message(self, message: str) -> None:
        result = f"{self.name}: Hi, my name is {self.name} :D"
        print(result)