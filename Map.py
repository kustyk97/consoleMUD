from Location import Location
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
        self.locations = np.array([[Location(self.NPCs) for _ in range(2)] for _ in range(2)])

    def get_location(self, coord: list) -> Location:
        try:
            location = self.locations[coord[0], coord[1]]
            print(f"Get Location {location}")
            return location
        except IndexError:
            print(f"Invalid coordinates: {coord}")
            return None