import unittest
from MUD.Character import Character
from unittest.mock import patch


class TestCharacter(unittest.TestCase):

    @patch("builtins.print")
    def setUp(self, mock_print):
        self.person1 = Character(name="Hero", hp=100.0, damage=20.0, shield=0.1)
        self.person2 = Character(name="Villain", hp=80.0, damage=15.0, shield=0.2)

    def test_initialization(self):
        self.assertEqual(self.person1.name, "Hero")
        self.assertEqual(self.person1.hp, 100.0)
        self.assertEqual(self.person1.damage, 20.0)
        self.assertEqual(self.person1.shield, 0.1)
        self.assertTrue(self.person1.alive)

    @patch("builtins.print")
    def test_print_info(self, mock_print):

        self.person1.print_info()
        mock_print.assert_called_once_with(
            f"HP: 100.00\n" f"Damage: 20.00\n" f"Shield: 0.10\n"
        )

    def test_attack(self):
        self.assertEqual(self.person1.attack(), 20.0)
        self.assertEqual(self.person2.attack(), 15.0)

    @patch("builtins.print")
    def test_get_damage(self, mock_print):
        self.person1.get_damage(30.0)

        self.assertAlmostEqual(self.person1.hp, 73.0)

    @patch("builtins.print")
    def test_get_damage_and_die(self, mock_print):
        self.person1.get_damage(3000.0)
        self.assertFalse(self.person1.alive)

    @patch("builtins.print")
    def test_die(self, mock_print):
        # person1 should die after this attack
        self.person1.die()
        self.assertFalse(self.person1.alive)


if __name__ == "__main__":
    unittest.main()
