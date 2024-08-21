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