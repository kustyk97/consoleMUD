from Location import Location
import numpy as np


class Map:
    NPCs = [{"name": "John"},
        {"name": "Anakin"},
        {"name": "Ron"},
        {"name": "Harry"},
        {"name": "Tom"},
        {"name": "Johnatan"},
        {"name": "Roman"}]

    def __init__(self) -> None:

        self.locations = [[Location(self.NPCs), Location(self.NPCs)],
                          [Location(self.NPCs), Location(self.NPCs)]]
        #self.locations = np.array(self.locations)
        

    def get_location(self, coord: list) -> Location:
        try:
            print(f"Get Location {self.locations[coord[0]][coord[1]]}")
            location = self.locations[coord[0]][coord[1]]
            return location
        except:
            return None