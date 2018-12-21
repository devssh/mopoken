import unittest
import sys

sys.path.insert(0, '../python-server')
from parser import Parser
from pokemon import Pokemon, advantage_types
from poketype import poketypes
from permutations import permutations
from breeder import Breeder, breeder_types
from match import Match
from game import Game


class TestMethods(unittest.TestCase):
    def test_parser_returns_pokemon_list(self):
        self.assertEqual(str(Parser("Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12").pokemon_list),
                         "[Fire#10, Water#20, Fighting#6, Psychic#10, Electric#12]")

    def test_parser_throws_error_on_incorrect_string(self):
        with self.assertRaises(ValueError) as context:
            Parser("aoteuhseatouh")
        self.assertTrue('Incorrect input string' in str(context.exception))

    def test_parser_throws_error_on_wrong_count(self):
        with self.assertRaises(ValueError) as context:
            Parser("fire#10;water#20")
        self.assertTrue('Incorrect number of pokemon' in str(context.exception))

    def test_parser_throws_error_on_wrong_format(self):
        with self.assertRaises(ValueError) as context:
            Parser("fire#1;water2;fire3;water3;fire4")
        self.assertTrue('Incorrect format for pokemon' in str(context.exception))

    def test_pokemon_initialized_correctly(self):
        self.assertEqual(str(Pokemon('Fire', 20)), "Fire#20")

    def test_pokemon_throws_error_on_wrong_type(self):
        wrong_type = "fireshock"
        with self.assertRaises(ValueError) as context:
            Pokemon(wrong_type, 20)
        self.assertTrue('Unknown type of pokemon: ' + wrong_type in str(context.exception))

    def test_pokemon_throws_error_on_wrong_type(self):
        wrong_level = "twenty"
        with self.assertRaises(ValueError) as context:
            Pokemon('Fire', wrong_level)
        self.assertTrue('Level of pokemon is not a number: ' + wrong_level in str(context.exception))

    def test_pokemon_at_disadvantage_type(self):
        self.assertEqual(Pokemon('Fire', 20).check_odds(Pokemon('Water', 20)), "Disadvantage")

    def test_pokemon_level_balance_to_type(self):
        self.assertEqual(Pokemon('Fire', 40).check_odds(Pokemon('Water', 20)), "Draw")

    def test_pokemon_level_overcome_type(self):
        self.assertEqual(Pokemon('Fire', 41).check_odds(Pokemon('Water', 20)), "Advantage")
        self.assertEqual(Pokemon('Water', 20).check_odds(Pokemon('Fighting', 100)), "Disadvantage")

    def test_pokemon_level_advantage(self):
        self.assertEqual(Pokemon('Fire', 21).check_odds(Pokemon('Fighting', 20)), "Advantage")
        self.assertEqual(Pokemon('Fire', 21).check_odds(Pokemon('Fire', 20)), "Advantage")

    def test_pokemon_level_equal(self):
        self.assertEqual(Pokemon('Fire', 20).check_odds(Pokemon('Fighting', 20)), "Draw")

    def test_pokemon_level_disadvantage(self):
        self.assertEqual(Pokemon('Fire', 19).check_odds(Pokemon('Fighting', 20)), "Disadvantage")
        self.assertEqual(Pokemon('Fire', 19).check_odds(Pokemon('Fire', 20)), "Disadvantage")

    def test_poketype(self):
        self.assertEqual(str(poketypes["Fire"].weaker_types), "['Grass', 'Ghost']")
        self.assertEqual(str(poketypes["Water"].weaker_types), "['Fire']")
        self.assertEqual(str(poketypes["Grass"].weaker_types), "['Electric', 'Fighting']")
        self.assertEqual(str(poketypes["Electric"].weaker_types), "['Water']")
        self.assertEqual(str(poketypes["Psychic"].weaker_types), "['Ghost']")
        self.assertEqual(str(poketypes["Ghost"].weaker_types), "['Fighting', 'Fire', 'Electric']")
        self.assertEqual(str(poketypes["Fighting"].weaker_types), "['Electric']")

    def test_permutations(self):
        self.assertEqual(list(permutations([1, 2, 3], 3)),
                         [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])

    def test_breeder_init_correctly(self):
        self.assertEqual(str(Breeder("npc",
                                     [Pokemon("Fire", 10), Pokemon("Water", 11), Pokemon("Grass", 12),
                                      Pokemon("Electric", 13),
                                      Pokemon("Psychic", 14)]
                                     )), "npc[Fire#10, Water#11, Grass#12, Electric#13, Psychic#14]")

    def test_breeder_correct_pokemon_count(self):
        with self.assertRaises(ValueError) as context:
            Breeder("player",
                    [Pokemon("Fire", 10)]
                    )
        self.assertTrue("Incorrect number of pokemon for breeder" in str(context.exception))

    def test_breeder_unique_pokemon_type(self):
        with self.assertRaises(ValueError) as context:
            Breeder("npc",
                    [Pokemon("Fire", 10), Pokemon("Fire", 10), Pokemon("Electric", 10), Pokemon("Grass", 10),
                     Pokemon("Water", 10)]
                    )
        self.assertTrue("A breeder can hold a maximum of one pokemon of each type" in str(context.exception))

    def test_integration_breeder_type_player_wins_if_possible(self):
        input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
        input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
        player1 = Breeder(breeder_types[1], Parser(input1).pokemon_list)
        npc_player2 = Breeder(breeder_types[0], Parser(input2).pokemon_list)
        battle_order = player1.fight(npc_player2)
        battle_results = [pokemon1.check_odds(pokemon2) for (pokemon1, pokemon2) in battle_order]
        wins = len([result for result in battle_results if advantage_types[1] == result])
        self.assertTrue(wins >= 3)

    def test_integration_breeder_type_player_loses_if_not_possible_to_win(self):
        input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
        input2 = "Water#100;Fighting#100;Psychic#100;Fire#120;Grass#20"
        player1 = Breeder(breeder_types[1], Parser(input1).pokemon_list)
        npc_player2 = Breeder(breeder_types[0], Parser(input2).pokemon_list)
        battle_order = player1.fight(npc_player2)
        battle_results = [(pokemon1.check_odds(pokemon2), pokemon1, pokemon2) for (pokemon1, pokemon2) in battle_order]
        wins = len([result for result in battle_results if advantage_types[1] == result])
        self.assertTrue(wins < 3)

    def test_integration_match_results_correctly(self):
        input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
        input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
        player1 = Breeder(breeder_types[1], Parser(input1).pokemon_list)
        npc_player2 = Breeder(breeder_types[0], Parser(input2).pokemon_list)
        results = Match(player1, npc_player2).results()
        self.assertEqual(str(results[0]), "player[Fire#10, Water#20, Fighting#6, Psychic#10, Electric#12]")
        self.assertEqual(str(results[1]), "[Fire#10, Water#20, Electric#12, Fighting#6, Psychic#10]")

        input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
        input2 = "Water#100;Fighting#100;Psychic#100;Fire#12;Grass#2"
        player1 = Breeder(breeder_types[1], Parser(input1).pokemon_list)
        npc_player2 = Breeder(breeder_types[0], Parser(input2).pokemon_list)
        results = Match(player1, npc_player2).results()
        self.assertEqual(str(results[0]), "npc[Water#100, Fighting#100, Psychic#100, Fire#12, Grass#2]")
        self.assertEqual(str(results[1]), "[Water#100, Fighting#100, Psychic#100, Fire#12, Grass#2]")

    def test_integration_game_results_correctly(self):
        input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
        input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
        self.assertEqual(Game().start(input1, input2),
                         "The winning order is Electric#12;Fire#10;Fighting#6;Water#20;Psychic#10")

    def test_integration_game_results_correctly(self):
        input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
        input2 = "Water#100;Fighting#100;Psychic#100;Fire#12;Grass#2"
        self.assertEqual(Game().start(input1, input2), "There are no chances of winning")


if __name__ == '__main__':
    unittest.main()
