import unittest
from unittest.mock import patch, MagicMock
from MUD.Character import Character
from MUD.NPC import NPC
from MUD.Location import Location
from MUD.Map import Map
from MUD.Player import Player  
import numpy as np

class TestPlayer(unittest.TestCase):

    @patch('builtins.print')
    def setUp(self, mock_print):
        self.player = Player(start_coords=[0, 0])

    def test_initialization(self):
        self.assertEqual(self.player.name, "Player")
        self.assertEqual(self.player.hp, 100)
        self.assertIsInstance(self.player, Character)
        self.assertEqual(self.player.coords, [0, 0])

        self.assertGreaterEqual(self.player.damage, 30)
        self.assertLessEqual(self.player.damage, 100)
        self.assertGreaterEqual(self.player.shield, 0.15)
        self.assertLessEqual(self.player.shield, 0.30)

    def test_write_message(self):
        input_values = ["test", "HelloThere"]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                result = self.player.write_message()
                self.assertEqual(result, input_value)

if __name__ == '__main__':
    unittest.main()