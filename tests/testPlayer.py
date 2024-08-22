import unittest
from unittest.mock import patch, MagicMock
from MUD.Character import Person
from MUD.NPC import NPC
from MUD.Location import Location
from MUD.Map import Map
from MUD.Player import Player  
import numpy as np

class TestPlayer(unittest.TestCase):

    @patch('builtins.print')
    def setUp(self, mock_print):
        self.map = Map()
        #create location with test NPC
        self.map.locations = np.array([[Location(name="testLocation1", npcs=[{"name": "Goblin1"}]), Location(name="testLocation2", npcs=[{"name": "Goblin2"}])], 
                               [Location(name="testLocation3", npcs=[{"name": "Goblin3"}]), Location(name="testLocation4", npcs=[{"name": "Goblin4"}])]])
        #self.map.locations[0][0] = Location(name="testLocation", npcs=[{"name": "Goblin"}])
        self.player = Player(game_map=self.map, coords=[0, 0])

    def test_initialization(self):
        self.assertEqual(self.player.name, "Player")
        self.assertEqual(self.player.hp, 100)
        self.assertIsInstance(self.player, Person)
        self.assertEqual(self.player.coords, [0, 0])
        self.assertIsInstance(self.player.location, Location)

        self.assertGreaterEqual(self.player.damage, 0)
        self.assertLessEqual(self.player.damage, 100)
        self.assertGreaterEqual(self.player.shield, 0)
        self.assertLessEqual(self.player.shield, 0.15)

    @patch('builtins.print')
    def test_describe_location(self, mock_print):
        self.player.describe_location()
        mock_print.assert_any_call("You are in location: testLocation1")
        mock_print.assert_any_call("Location testLocation1 contains 1 NPCs")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['0', 'Hello!']) 
    def test_interact_with_npc(self, mock_input, mock_print):
        self.player.interact_with_npc()
        mock_print.assert_called_with("Goblin1: Hi, my name is Goblin1 :D")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1']) 
    def test_move_succesed(self, mock_input, mock_print):
        self.player.coords = [0,0]
        self.player.move()
        mock_print.assert_called_with("Successfully moved")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1'])  
    def test_move_invalid(self, mock_input, mock_print):
        self.player.coords = [2, 2] 
        self.player.move()
        mock_print.assert_called_with("Failed to move")

    @patch('builtins.print')
    def test_start_fight(self, mock_print):
        
        npc = NPC(name="Goblin")
        self.player.start_fight(npc)
        mock_print.assert_any_call("Start fight with Goblin")

    @patch('builtins.print')
    def test_end_game(self, mock_print):
        with self.assertRaises(SystemExit):
            self.player.end_game()
        mock_print.assert_any_call("Game ended.")
        mock_print.assert_any_call("Bye")

if __name__ == '__main__':
    unittest.main()