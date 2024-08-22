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

    def move(self) -> None:
        directions = {
            1: self.move_north,
            2: self.move_south,
            3: self.move_west,
            4: self.move_east
        }

        print("Choose direction:")
        for key, direction in directions.items():
            print(f"{key}. {direction.__name__.replace('_', ' ').title()}")
        print("Insert value of destination directin:", end=" ")
        value = int(input())

        move_action = directions.get(value)
        if move_action and move_action():
            print("Successfully moved")
        else:
            print("Failed to move")

    def move_north(self) -> bool:
        return self.move_to([self.coords[0] - 1, self.coords[1]])

    def move_south(self) -> bool:
        return self.move_to([self.coords[0] + 1, self.coords[1]])

    def move_west(self) -> bool:
        return self.move_to([self.coords[0], self.coords[1] - 1])

    def move_east(self) -> bool:
        return self.move_to([self.coords[0], self.coords[1] + 1])

    def move_to(self, new_coords: list) -> bool:
        if self.map.get_location(new_coords) is None:
            return False
        self.coords = new_coords
        self.location = self.map.get_location(self.coords)
        return True

    def write_message(self, npc: NPC) -> None:
        print("Insert message:", end=" ")
        text = input()
        npc.message(text)

    def start_fight(self, opponent: NPC) -> None:
        print(f"Start fight with {opponent.name}")
        opponent.get_damage(self.attack(), self)



