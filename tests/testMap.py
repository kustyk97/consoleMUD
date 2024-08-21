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

    def test_npcs_in_locations(self):
        for i in range(2):
            for j in range(2):
                location = self.map.locations[i, j]
                self.assertEqual(len(location.npcs), len(Map.NPCs))
                for npc in location.npcs:
                    self.assertIsInstance(npc, NPC)

if __name__ == '__main__':
    unittest.main()