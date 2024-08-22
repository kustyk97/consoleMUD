from MUD.NPC import NPC

class Location:
    def __init__(self, name: str, npcs: list) -> None:
        self.npcs = [NPC(npc["name"]) for npc in npcs]
        self.name = name
        print("Created new Location")

    def get_list_of_npcs(self) -> list:
        return self.npcs

    def __str__(self) -> str:
        return f"Location {self.name} contains {len(self.npcs)} NPCs"
    
    def get_name(self) -> str:
        return self.name
    
    def send_message_to_NPC(self, message: str, npc_ID: int) -> None:
        self.npcs[npc_ID].message(message)

    def get_NPC(self, npc_ID: int) -> NPC:
        return self.npcs[npc_ID]
    
    def damage_NPC(self, damage_value: float, npc_ID: int) -> None:
        self.npcs[npc_ID].get_damage(damage=damage_value)
    