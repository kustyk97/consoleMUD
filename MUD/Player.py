from MUD.Person import Person
from MUD.NPC import NPC
import random as rnd
from MUD.Location import Location
from MUD.Map import Map

class Player(Person):
    def __init__(self, game_map: Map, coords: list) -> None:
        damage = rnd.uniform(0, 100)
        shield = rnd.uniform(0, 0.15)
        super().__init__("Player", 100, damage, shield)

        self.coords = coords
        self.map = game_map
        self.location = self.map.get_location(coords)

    def start_play(self) -> None:
        actions = {
            1: self.describe_location,
            2: self.interact_with_npc,
            3: self.fight_npc,
            4: self.move,
            5: self.end_game
        }

        while True:
            print("Possible actions:")
            for key, action in actions.items():
                print(f"{key}. {action.__name__.replace('_', ' ').title()}")
            print("Insert number of chosen action:", end=" ")
            value = int(input())

            action = actions.get(value)
            if action:
                action()
            else:
                print("Unknow value, insert again")

    def describe_location(self) -> None:
        # Implementacja opisu lokacji
        print(f"You are in location: {self.location.name}")
        print(self.location.__str__())

    def interact_with_npc(self) -> None:
        self.choose_npc("Which NPC do you want to interact with?", self.location.get_list_of_npcs(), self.write_message)

    def fight_npc(self) -> None:
        self.choose_npc("Which NPC do you want to fight?", self.location.get_list_of_npcs(), self.start_fight)

    def choose_npc(self, prompt: str, npcs: list, action) -> None:
        print(prompt)
        for i, npc in enumerate(npcs):
            print(f"{i}: {npc.name}")
        print("Insert value:", end=" ")
        npc_id = int(input())

        if 0 <= npc_id < len(npcs):
            action(npcs[npc_id])
        else:
            print("Unknow number")
            print("Return to main menu")

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

    def end_game(self) -> None:
        print("Game ended.")
        print("Bye")
        exit()

