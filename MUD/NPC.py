from MUD.Character import Character
import random as rnd


class NPC(Character):
    def __init__(self, name: str) -> None:
        damage = rnd.uniform(0, 100)
        shield = rnd.uniform(0, 0.15)
        super().__init__(name, 100, damage, shield)
        print(
            f"Created NPC with name {self.name}, damage {self.damage:.2f}, and shield {self.shield:.2f}"
        )

    def message(self, message: str) -> None:
        print(f"{self.name}: Hi, my name is {self.name} :D")
