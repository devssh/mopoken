from pokemon import Pokemon
from permutations import permutations
from pokemon import advantage_types
from match import min_wins_to_victory

max_pokemon_count = 5

breeder_types = ["npc", "player"]


class Breeder:
    def __init__(self, type, pokemon_list):
        if len(pokemon_list) != max_pokemon_count:
            raise ValueError("Incorrect number of pokemon for breeder")
        if len(list(set([pokemon.type for pokemon in pokemon_list]))) != max_pokemon_count:
            raise ValueError("A breeder can hold a maximum of one pokemon of each type")
        if type not in breeder_types:
            raise ValueError("Invalid type of breeder")
        self.type = type
        self.pokemon_list = pokemon_list

    def __str__(self):
        return str(self.type) + str(self.pokemon_list)

    def __repr__(self):
        return str(self.type) + str(self.pokemon_list)

    def fight(self, other):
        def advantageous_fight_order(breeder1, breeder2):
            breeder1_pokemon = breeder1.pokemon_list
            breeder2_pokemon = breeder2.pokemon_list
            sample_space = [list(zip(x, breeder2_pokemon)) for x in permutations(breeder1_pokemon, len(breeder1_pokemon))]
            outcomes = [len(["win" for duel in combination if duel[0].check_odds(duel[1]) == advantage_types[1]])
                        for combination in sample_space]
            wins = [sample_space[index] for index, outcome in enumerate(outcomes) if outcome >= min_wins_to_victory]
            return [duel[0] for duel in wins[0]] if len(wins) > 0 else breeder1.pokemon_list

        def select_pokemon_order(breeder1, breeder2):
            if breeder1.type == breeder_types[0]:
                return breeder1.pokemon_list
            else:
                return advantageous_fight_order(breeder1, breeder2)

        breeder1_pokemon = select_pokemon_order(self, other)
        breeder2_pokemon = select_pokemon_order(other, self)

        return list(zip(breeder1_pokemon, breeder2_pokemon))


if __name__ == '__main__':
    print(Breeder(
        [Pokemon("Fire", 10), Pokemon("Water", 11), Pokemon("Grass", 12), Pokemon("Electric", 13),
         Pokemon("Psychic", 14)]
    ))
