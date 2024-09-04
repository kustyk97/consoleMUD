import unittest
from unittest.mock import patch
from MUD.Game import Game
from MUD.NPC import NPC

class TestGame(unittest.TestCase):

    @patch('builtins.print')
    def setUp(self, mock_print) -> None:
        self.game = Game()
        self.game.map.locations[0,0].name = 'Test Location'
        self.game.map.locations[0,0].npcs[0].name = "Goblin"
        return super().setUp()

    def test_init(self):
        self.assertIsNotNone(self.game.map)
        self.assertIsNotNone(self.game.player)
        self.assertEqual(self.game.player.coords, [0,0])

    @patch('builtins.print')
    def test_describe_location(self, mock_print):
        self.game.player.coords = [0,0]
        self.game.describe_location()
        mock_print.assert_any_call("Location have coords: [0, 0]")
        mock_print.assert_any_call("You are in location: Test Location")

    @patch('builtins.print')
    def test_interact_with_npc_invalid(self, mock_print):
        input_values = [-1, "s", "Hello There", " ", ""]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.interact_with_npc()
                mock_print.assert_any_call("Unknow number")
                mock_print.assert_any_call("Return to main menu")

    # @patch('builtins.input', side_effect=[0])  # Choose invalid NPC ID
    @patch.object(Game, 'write_message')
    @patch('builtins.print')
    def test_interact_with_npc_valid(self, mock_print, mock_write_message):
        input_values = [0]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.interact_with_npc()
                mock_write_message.assert_called_once()

    @patch('builtins.print')
    def test_fignt_npc_invalid(self, mock_print):
        input_values = [-1, "s", "Hello There", " ", ""]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.fight_npc()
                mock_print.assert_any_call("Unknow number")
                mock_print.assert_any_call("Return to main menu")

    @patch.object(Game, 'write_message')
    @patch('builtins.print') 
    def test_fignt_npc_valid(self, mock_print, mock_start_fight):
        input_values = [0]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.interact_with_npc()
                mock_start_fight.assert_called_once()
    @patch('builtins.print')
    def test_write_message(self, mock_print):

        with patch('builtins.input', return_value="test"):
            self.game.write_message([0,0], 0)
        printed_messages = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue(any("Insert message:" in message for message in printed_messages))

    @patch('builtins.print')
    def test_start_fight(self, mock_print):

        self.game.start_fight([0,0], 0)
        mock_print.asserty_anu_call("Start fight with Goblin")        

    @patch('builtins.print')
    def test_choose_npc_valid(self, mock_print):
        input_values = [0]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.choose_npc("Which NPC do you want to fight?", [0,0], self.game.start_fight )
                self.assertFalse(mock_print.call_args_list and any("Unknow number" in call[0][0] for call in mock_print.call_args_list))
                self.assertFalse(mock_print.call_args_list and any("Return to main menu" in call[0][0] for call in mock_print.call_args_list))

    
    @patch('builtins.print')
    def test_choose_npc_invalid(self, mock_print):

        input_values = [-1, "s", "Hello There", " ", ""]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.choose_npc("Which NPC do you want to fight?", [0,0], self.game.start_fight )
                mock_print.assert_any_call("Unknow number")
                mock_print.assert_any_call("Return to main menu")

    def test_get_list_of_NPC_in_location(self):
        NPCs = [
        {"name": "Goblin"},
        {"name": "Anakin"},
        {"name": "Ron"},
        {"name": "Harry"},
        {"name": "Tom"},
        {"name": "Johnatan"},
        {"name": "Roman"}
        ]

        npc_list = self.game.get_list_of_NPC_in_location([0,0])
        self.assertEqual(len(npc_list), 7)
        for npc, npc_names in zip(npc_list, NPCs):
            self.assertEqual(npc.name, npc_names["name"])
   
    @patch.object(Game, 'move_north')
    @patch.object(Game, 'move_south')
    @patch.object(Game, 'move_west')
    @patch.object(Game, 'move_east')
    @patch('builtins.print')
    def test_move_valid(self,mock_print , mock_move_east, mock_move_west, mock_move_south, mock_move_north):
        mock_move_north.__name__ = 'move_north'
        mock_move_south.__name__ = 'move_south'
        mock_move_west.__name__ = 'move_west'
        mock_move_east.__name__ = 'move_east'
        input_values = {
            1: mock_move_north,
            2: mock_move_south,
            3: mock_move_west,
            4: mock_move_east
                        }
        for input_value, action in input_values.items():
            with patch('builtins.input', return_value=input_value):
                self.game.move()
                action.assert_called_once()
                # mock_print.assert_any_call("Successfully moved")
    
    @patch('builtins.print')
    def test_move_invalid(self, mock_print):

        input_values = [-1, "s", "Hello There", " ", ""]
        for input_value in input_values:
            with patch('builtins.input', return_value=input_value):
                self.game.move()
                mock_print.assert_any_call("Failed to move")

    def test_move_north(self):
        pass

    def test_move_to_valid(self):
        cases = [[0,0], [1,1]]
        for case in cases:
            self.assertTrue(self.game.move_to(case))
    @patch('builtins.print')
    def test_move_to_invalid(self, mock_print):
        cases = [[-1, 0 ], [10, 10]]
        for case in cases:
            self.assertFalse(self.game.move_to(case))


    @patch('builtins.print')
    def test_start_fight(self, mock_print):
        

        npc = NPC(name="Goblin")
        self.game.map.locations[0,0].npcs[0] = npc
        self.game.start_fight([0,0], 0)
        mock_print.assert_any_call("Start fight with Goblin")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[1])  # Choose end_game
    def test_end_game(self, mock_input, mock_print):
        with self.assertRaises(SystemExit):  # end_game calls exit()
            self.game.end_game()

        mock_print.assert_any_call("Game ended.")
        mock_print.assert_any_call("Bye")

if __name__=='__main__':
    unittest.main()
