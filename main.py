from MUD.Map import Map
from MUD.Player import Player

def main():
    print("Welcome in consoleMUD :D")

    map = Map()
    player = Player(map, [0,0])
    player.start_play()

if __name__=="__main__":
    main()