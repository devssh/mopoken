from pokemon import advantage_types
import random

min_wins_to_victory = 3


class Match:
    def __init__(self, breeder1, breeder2):
        self.breeder1 = breeder1
        self.breeder2 = breeder2

    def decide_winner(self):
        wins = len([result for result in self.battle_results if advantage_types[1] == result])
        losses = len([result for result in self.battle_results if advantage_types[-1] == result])
        self.victor = 1 if wins >= min_wins_to_victory else 2 if losses >= min_wins_to_victory else random.randint(1, 2)
        return self.breeder1 if self.victor == 1 else self.breeder2

    def results(self):
        self.battle_order = self.breeder1.fight(self.breeder2)
        self.battle_results = [pokemon1.check_odds(pokemon2) for (pokemon1, pokemon2) in self.battle_order]

        return (self.decide_winner(),
                [pokemon1 if self.victor == 1 else pokemon2 for (pokemon1, pokemon2) in self.battle_order])


if __name__ == '__main__':
    from breeder import Breeder, breeder_types
    from parser import Parser

    input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
    input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
    player1 = Breeder(breeder_types[1], Parser(input1).pokemon_list)
    npc_player2 = Breeder(breeder_types[0], Parser(input2).pokemon_list)
    print(Match(player1, npc_player2).results())
