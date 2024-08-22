import unittest
import numpy as np
from MUD.Location import Location
from MUD.Map import Map
from unittest.mock import patch
from MUD.NPC import NPC

class TestMap(unittest.TestCase):
    
    @patch('builtins.print')
    def setUp(self,mock_print):
        self.map = Map()
        self.map.locations[0,0].npcs[0].name = "NPC1"
        self.map.locations[0,0].npcs[0].shield = 0

    def test_init(self):
        self.assertEqual(self.map.locations.shape, (2, 2))
        self.assertIsInstance(self.map.locations[0, 0], Location)

    @patch('builtins.print')
    def test_get_location_valid(self,mock_print):
        location = self.map.get_location([0, 1])
        self.assertIsInstance(location, Location)
        self.assertEqual(location.name, "Location")

    @patch('builtins.print')
    def test_get_location_invalid(self,mock_print):
        location = self.map.get_location([2, 2])
        self.assertIsNone(location)
        location = self.map.get_location([-1, -1])
        self.assertIsNone(location)

    def test_npcs_in_locations(self):
        for i in range(2):
            for j in range(2):
                location = self.map.locations[i, j]
                self.assertEqual(len(location.npcs), len(Map.NPCs))
                for npc in location.npcs:
                    self.assertIsInstance(npc, NPC)

    def test_get_location_name(self):
        self.assertEqual(self.map.get_location_name([0,0]), "Location")

    @patch('builtins.print')        
    def test_send_message_to_NPC(self, mock_print):
        self.map.send_message_to_NPC("TestMessage", NPC_coords=[0,0], npc_ID=0)
        mock_print.assert_called_once_with(f"NPC1: Hi, my name is NPC1 :D")
        
    def test_get_NPC(self):
        npc = self.map.get_NPC(NPC_coords=[0,0], npc_ID=0)
        self.assertIsInstance(npc, NPC)
        self.assertEqual(npc.name, "NPC1")

    @patch('builtins.print')
    def test_damage_NPC(self, mock_print):
        self.map.damage_NPC(10, NPC_coords=[0,0], npc_ID=0)
        self.assertEqual(self.map.locations[0,0].npcs[0].hp, 90)

if __name__ == '__main__':
    unittest.main()