import unittest
from unittest.mock import patch
import random as rnd
from MUD.NPC import NPC
from MUD.Character import Character


class TestNPC(unittest.TestCase):

    @patch("builtins.print")
    def setUp(self, mock_print):
        rnd.seed(0)
        self.npc = NPC(name="Goblin")

    def test_initialization(self):
        # Check name, hp and instance
        self.assertEqual(self.npc.name, "Goblin")
        self.assertEqual(self.npc.hp, 100)
        self.assertIsInstance(self.npc, Character)

        # Check range of damege and shield
        self.assertGreaterEqual(self.npc.damage, 0)
        self.assertLessEqual(self.npc.damage, 100)
        self.assertGreaterEqual(self.npc.shield, 0)
        self.assertLessEqual(self.npc.shield, 0.15)

    @patch("builtins.print")
    def test_message(self, mock_print):
        self.npc.message("Hello!")
        mock_print.assert_called_once_with("Goblin: Hi, my name is Goblin :D")


if __name__ == "__main__":
    unittest.main()
