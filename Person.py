
class Person:
    name = None
    alive = True
    hp = None
    damage = None
    shield = None
    locationId = None

    def __init__(self, name: str, hp: float, damage: float, shield: float, locationId: int) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        self.shield = shield
        self.locationId = locationId
        pass
    
    def print_info(self) -> None:
        result = f"HP: {self.hp}\ndamage: {self.damage}\nshield: {self.shield}\nlocation: {self.location}"
        print(result)

    def attack(self) -> float:
        return self.damage

    def get_damage(self, damage: float, oponent): 
        damage = damage*(1-self.shield)
        self.hp -=damage
        print(f"{self.name} get damege and have {self.hp} hp after this")
        if self.hp <= 0:
            self.die()
            return 
        else:
            oponent.get_damage(self.attack(), self)
            return 

    def die(self):
        self.alive = False
        print(f"{self.name} die!!!")
