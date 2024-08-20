from NPC import NPC

class Location:

    def __init__(self, npcs: list) -> None:
        self.npcs = []
        for npc in npcs:
            npc_object = NPC(npc["name"])
            self.npcs.append(npc_object)
        print("Created new Location")
            
    def get_list_of_npc(self) -> list:
        return self.npcs
    
    def __str__(self) -> str:
        return f"Location contain {len(self.npcs)} NPC"