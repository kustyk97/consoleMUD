from Person import Person
from NPC import NPC
import random as rnd
from Location import Location
from Map import Map


class Player(Person):

    def __init__(self, map: Map, coords: list) -> None:
        damage = rnd.uniform(0, 100)
        shield = rnd.uniform(0, 0.15)
        super().__init__("Player", 100, damage, shield, 1)

        self.coords = coords
        self.map = map
        self.location = self.map.get_location(coords)

    def start_play(self) -> None:

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
                i = 0
                for npc in npcs:
                    print(f"{i}: {npc.name}")
                    i +=1
                npcId = int(input())
                if type(npcId) != int:
                    print("Nie rozponałem numeru")
                elif value == 2:
                    self.write_message(npcs[npcId])
                else:
                    self.start_fight(npcs[npcId])
            elif value == 4:
                self.move()
                continue
            elif value == 5:
                break
            else:
                print("Nie rozpoznałem numeru akcji, spróbuj ponownie")
                continue

    def move(self):
        print(f"1.Idź na północ")
        print(f"2.Idź na południe")
        print(f"3.Idź na zachód")
        print(f"4.Idź na wschód")
        print("Wpisz numer kierunku w który chcesz się przemieścić:", end=" ")
        value = int(input())
        if value == 1:
            result = self.move_north()
        elif value == 2:
            result = self.move_south()
        elif value == 3:
            result = self.move_west()
        elif value == 4:
            result = self.move_east()
        else:
            print("Nie rozponałem numeru")
            return
        if result == True:
            print("Pomyślnie przemieściłeś się")
        else:
            print("Nie udało się przemieścić")
        return

    def move_north(self) ->bool:
        if self.map.get_location([self.coords[0]-1, self.coords[1]]) == None:
            return False
        else:
            self.coords = [self.coords[0]-1, self.coords[1]]
            self.location = self.map.get_location(self.coords)
            return True
        
    def move_south(self) ->bool:
        if self.map.get_location([self.coords[0]+1, self.coords[1]]) == None:
            return False
        else:
            self.coords = [self.coords[0]+1, self.coords[1]]
            self.location = self.map.get_location(self.coords)
            return True
        
    def move_west(self) ->bool:
        if self.map.get_location([self.coords[0], self.coords[1]]-1) == None:
            return False
        else:
            self.coords = [self.coords[0], self.coords[1]-1]
            self.location = self.map.get_location(self.coords)
            return True
        
    def move_east(self) ->bool:
        if self.map.get_location([self.coords[0], self.coords[1]+1]) == None:
            return False
        else:
            self.coords = [self.coords[0], self.coords[1]+1]
            self.location = self.map.get_location(self.coords)
            return True

    def write_message(self, npc: NPC) -> None:
        print("Wpisz treść wiadomości:", end=" ")
        text = input()
        npc.message(text)

    def start_fight(self, opponent: NPC) -> None:
        print(f"Rozpoczynam walkę z {opponent.name}")
        opponent.get_damage(self.attack(), self)