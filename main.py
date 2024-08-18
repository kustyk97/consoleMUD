from Location import Location
from Map import Map
from Player import Player
from NPC import NPC

NPCs = [{"name": "John"},
        {"name": "Anakin"},
        {"name": "Ron"},
        {"name": "Harry"},
        {"name": "Tom"},
        {"name": "Johnatan"},
        {"name": "Roman"}]

def main():
    print("Hello there")
    location = Location(NPCs)
    player = Player(location)
    player.start_play()

if __name__=="__main__":
    main()