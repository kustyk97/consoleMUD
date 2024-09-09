class Character:
    def __init__(self, name: str, hp: float, damage: float, shield: float) -> None:
        self.alive = True
        self.name = name
        self.hp = hp
        self.damage = damage
        self.shield = shield

    def print_info(self) -> None:
        result = (
            f"HP: {self.hp:.2f}\n"
            f"Damage: {self.damage:.2f}\n"
            f"Shield: {self.shield:.2f}\n"
        )
        print(result)

    def attack(self) -> float:
        return self.damage

    def get_damage(self, damage: float) -> None:
        effective_damage = damage * (1 - self.shield)
        self.hp -= effective_damage

        print(
            f"Oponent attacks with damage {effective_damage:.2f} and {self.name} now has {self.hp:.2f} HP after this attack."
        )

        if self.hp <= 0:
            self.die()

    def die(self) -> None:
        self.alive = False
        print(f"{self.name} has died!!!")
