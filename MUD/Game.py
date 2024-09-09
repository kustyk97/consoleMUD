from MUD.Map import Map
from MUD.Player import Player
from MUD.Location import Location
from MUD.NPC import NPC
from utils.utils import try_get_int_value


class Game:

    def __init__(self) -> None:
        self.map = Map()
        self.player = Player(start_coords=[0, 0])
        pass

    def start(self) -> None:

        actions = {
            1: self.describe_location,
            2: self.interact_with_npc,
            3: self.fight_npc,
            4: self.move,
            5: self.end_game,
        }

        while True:
            print("Possible actions:")
            for key, action in actions.items():
                print(f"{key}. {action.__name__.replace('_', ' ').title()}")
            print("Insert number of chosen action:", end=" ")
            value = try_get_int_value()
            if value is not None:
                action = actions.get(value)
                if action:
                    action()
                else:
                    print("Unknow value, insert again")
            else:
                print("Unknow value, insert again")

    def describe_location(self) -> None:
        print(f"Location have coords: {self.player.coords}")
        location = self.map.get_location(self.player.coords)
        # Implementacja opisu lokacji
        print(f"You are in location: {location.get_name()}")
        print(location.__str__())

    def interact_with_npc(self) -> None:
        self.choose_npc(
            "Which NPC do you want to interact with?",
            self.player.coords,
            self.write_message,
        )

    def fight_npc(self) -> None:
        self.choose_npc(
            "Which NPC do you want to fight?", self.player.coords, self.start_fight
        )

    def write_message(self, NPC_coords: list, npc_ID: int) -> None:
        message_text = self.player.write_message()
        self.map.send_message_to_NPC(message_text, NPC_coords, npc_ID)

    def start_fight(self, NPC_coords: list, opponent_ID: int) -> None:
        print(
            f"Start fight with {self.map.get_NPC(NPC_coords=NPC_coords, npc_ID=opponent_ID).name}"
        )

        while (
            self.player.alive is True
            and self.map.get_NPC(NPC_coords=NPC_coords, npc_ID=opponent_ID).alive
            is True
        ):
            print(f"{self.player.name} attack")
            self.map.damage_NPC(self.player.attack(), NPC_coords, opponent_ID)
            if (
                self.map.get_NPC(NPC_coords=NPC_coords, npc_ID=opponent_ID).alive
                is True
            ):
                print(f"Oponent attack")
                self.player.get_damage(
                    self.map.get_NPC(NPC_coords=NPC_coords, npc_ID=opponent_ID).attack()
                )

    def choose_npc(self, prompt: str, coords: list, action) -> None:
        print(prompt)
        npcs = self.get_list_of_NPC_in_location(self.player.coords)
        for i, npc in enumerate(npcs):
            print(f"{i}: {npc.name}")
        print("Insert value:", end=" ")
        npc_id = try_get_int_value()

        if npc_id is not None:
            if 0 <= npc_id < len(npcs):
                action(coords, npc_id)
            else:
                print("Unknow number")
                print("Return to main menu")
        else:
            print("Unknow number")
            print("Return to main menu")

    def get_list_of_NPC_in_location(self, coords: list) -> list:
        return self.map.get_location(coord=coords).get_list_of_npcs()

    def move(self) -> None:
        directions = {
            1: self.move_north,
            2: self.move_south,
            3: self.move_west,
            4: self.move_east,
        }

        print("Choose direction:")
        for key, direction in directions.items():
            print(f"{key}. {direction.__name__.replace('_', ' ').title()}")
        print("Insert value of destination directin:", end=" ")
        value = try_get_int_value()

        if value is not None:
            move_action = directions.get(value)
            if move_action and move_action():
                print("Successfully moved")
            else:
                print("Failed to move")
        else:
            print("Failed to move")

    def move_north(self) -> bool:
        return self.move_to([self.player.coords[0] - 1, self.player.coords[1]])

    def move_south(self) -> bool:
        return self.move_to([self.player.coords[0] + 1, self.player.coords[1]])

    def move_west(self) -> bool:
        return self.move_to([self.player.coords[0], self.player.coords[1] - 1])

    def move_east(self) -> bool:
        return self.move_to([self.player.coords[0], self.player.coords[1] + 1])

    def move_to(self, new_coords: list) -> bool:
        if self.map.get_location(new_coords) is None:
            return False
        self.player.coords = new_coords
        return True

    def end_game(self) -> None:
        print("Game ended.")
        print("Bye")
        exit()
