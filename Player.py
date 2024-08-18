from Person import Person
from NPC import NPC
import random as rnd
from Location import Location
from Map import Map


class Player(Person):

    location = None
    def __init__(self, location: Location) -> None:
        damage = rnd.uniform(0, 100)
        shield = rnd.uniform(0, 0.15)
        super().__init__("Player", 100, damage, shield, 1)
        self.location = location

    def start_play(self) -> None:

        print("Witaj w grze consoleMUD :D")
        while True:
            print("Jaką akcję chcesz wykonać?")
            print("1. Dowiedz się więcej o lokacji w której jesteś")
            print("2. Zagadaj do NPC")
            print("3. Walcz z NPC")
            print("4. wyrusz do innej lokacji")
            print("5. Zakończ rozgrywkę")
            print("Wpisz numer akcji:", end=" ")
            value = int(input())
            if value == 1:
                continue
            if value in [2,3]:
                print("Z którym NPC chcesz wejść w interakcję?")
                print("NPC w tej lokacji")
                npcs = self.location.get_list_of_npc()
                i = 1
                for npc in npcs:
                    print(f"{i}: {npc.name}")
                    i +=1
                npcId = int(input())
                if type(npcId) != int:
                    print("Nie rozponałem numeru")
                elif value == 2:
                    self.write_message()
                else:
                    self.start_fight(npcs[npcId-1])
            elif value == 4:
                continue
            elif value == 5:
                break
            else:
                print("Nie rozpoznałem numeru akcji, spróbuj ponownie")
                continue

            

    def move(self):
        pass

    def write_message(self) -> None:
        text = input()

    def start_fight(self, opponent: NPC) -> None:
        opponent.get_damage(self.attack(), self)