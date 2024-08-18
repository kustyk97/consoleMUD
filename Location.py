from NPC import NPC

class Location:

    npcs = []

    def __init__(self, npcs) -> None:
        
        for npc in npcs:
            npc_object = NPC(npc["name"])
            self.npcs.append(npc_object)
            
    def get_list_of_npc(self) -> list:
        return self.npcs