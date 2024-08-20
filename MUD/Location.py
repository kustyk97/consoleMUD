from NPC import NPC

class Location:
    def __init__(self, npcs: list) -> None:
        self.npcs = [NPC(npc["name"]) for npc in npcs]
        self.name = "Location"
        print("Created new Location")

    def get_list_of_npcs(self) -> list:
        return self.npcs

    def __str__(self) -> str:
        return f"Location contains {len(self.npcs)} NPCs"