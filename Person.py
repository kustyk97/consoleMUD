
class Person:
    
    def __init__(self, name: str, hp: float, damage: float, shield: float, locationId: int) -> None:
        self.alive = True
        self.name = name
        self.hp = hp
        self.damage = damage
        self.shield = shield
        self.locationId = locationId
        pass
    
    def print_info(self) -> None:
        result = f"HP: {self.hp:.2f}\ndamage: {self.damage:.2f}\nshield: {self.shield:.2f}\nlocation: {self.location}"
        print(result)

    def attack(self) -> float:
        return self.damage

    def get_damage(self, damage: float, oponent): 
        damage = damage*(1-self.shield)
        self.hp -=damage

        print(f"{oponent.name} attack with damage {damage:.2f} and {self.name} get damege and have {self.hp:.2f} hp after this attack ")
        if self.hp <= 0:
            self.die()
            return 
        else:
            oponent.get_damage(self.attack(), self)
            return 

    def die(self):
        self.alive = False
        print(f"{self.name} die!!!")
