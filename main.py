from Location import Location
from Map import Map
from Player import Player
from NPC import NPC

def main():
    print("Welcome in consoleMUD :D")

    map = Map()
    player = Player(map, [0,0])
    player.start_play()

if __name__=="__main__":
    main()