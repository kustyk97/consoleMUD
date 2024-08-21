import unittest
from unittest.mock import patch
from MUD.NPC import NPC
from MUD.Location import Location

class TestLocation(unittest.TestCase):
    
    @patch('builtins.print')
    def setUp(self, mock_print):
        self.npcs = [
            {"name": "NPC1"},
            {"name": "NPC2"},
            {"name": "NPC3"}
        ]
        self.locaton_name = "TestLocation"
        self.location = Location(self.locaton_name, self.npcs)

    def test_init(self):
        self.assertEqual(len(self.location.npcs), 3)
        self.assertEqual(self.location.name, self.locaton_name)

    def test_get_list_of_npcs(self):
        npcs = self.location.get_list_of_npcs()
        self.assertEqual(len(npcs), 3)
        self.assertIsInstance(npcs[0], NPC)

    def test_str(self):
        self.assertEqual(str(self.location), f"Location {self.locaton_name} contains {len(self.npcs)} NPCs")

    def test_npc_creation(self):
        for npc in self.location.npcs:
            self.assertIsInstance(npc, NPC)

if __name__ == '__main__':
    unittest.main()