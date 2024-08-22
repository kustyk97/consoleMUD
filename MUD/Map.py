from MUD.Location import Location
from MUD.NPC import NPC
import numpy as np

class Map:
    NPCs = [
        {"name": "John"},
        {"name": "Anakin"},
        {"name": "Ron"},
        {"name": "Harry"},
        {"name": "Tom"},
        {"name": "Johnatan"},
        {"name": "Roman"}
    ]

    def __init__(self) -> None:
        self.locations = np.array([[Location("Location", self.NPCs) for _ in range(2)] for _ in range(2)])

    def get_location(self, coord: list) -> Location:
        if coord[0] < 0 or coord [1] < 0:            
            print(f"Invalid coordinates: {coord}")
            return None
        try:
            location = self.locations[coord[0], coord[1]]
            return location
        except IndexError:
            print(f"Invalid coordinates: {coord}")
            return None
    def get_location_name(self, coord: list)-> str:
        try:
            location = self.locations[coord[0], coord[1]]
            return location.get_name
        except IndexError:
            print(f"Invalid coordinates: {coord}")
            return None
        
    def send_message_to_NPC(self, message: str, NPC_coords: list, npc_ID: int) -> None:
        self.locations[NPC_coords[0], NPC_coords[1]].send_message_to_NPC(message, npc_ID)

    def get_NPC(self, NPC_coords: list, npc_ID: int) -> NPC:
        return self.locations[NPC_coords[0], NPC_coords[1]].get_NPC(npc_ID)
    
    def damage_NPC(self, damage_value: float, NPC_coords: list, npc_ID: int) -> None:
        self.locations[NPC_coords[0], NPC_coords[1]].damage_NPC(damage_value, npc_ID)