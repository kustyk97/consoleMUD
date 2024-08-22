from MUD.Character import Character
from MUD.NPC import NPC
import random as rnd
from MUD.Location import Location
from MUD.Map import Map

class Player(Character):
    def __init__(self, start_coords: list) -> None:
        damage = rnd.uniform(30, 100)
        shield = rnd.uniform(0.15, 0.30)
        super().__init__("Player", 100, damage, shield)

        self.coords = start_coords

    

    def write_message(self) -> str:
        print("Insert message:", end=" ")
        text = input()
        return text
    



