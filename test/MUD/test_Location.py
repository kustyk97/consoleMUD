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
        self.location.npcs[0].shield = 0.0

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
    def test_get_name(self):
        self.assertEqual(self.location.get_name(), self.locaton_name)

    @patch('builtins.print')
    def test_send_message_to_NPC(self, mock_print):
        self.location.send_message_to_NPC("TestMessage", 0)
        mock_print.assert_called_once_with(f"NPC1: Hi, my name is NPC1 :D")

    def test_get_NPC(self):
        npc = self.location.get_NPC(0)
        self.assertIsInstance(npc, NPC)
        self.assertEqual(npc.name, "NPC1")
    
    @patch('builtins.print')
    def test_damage_NPC(self, mock_print):
        self.location.damage_NPC(10, 0)
        self.assertEqual(self.location.npcs[0].hp, 90)

if __name__ == '__main__':
    unittest.main()