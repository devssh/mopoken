from pokemon import Pokemon
from permutations import permutations

class Breeder:
    def __init__(self, pokemon_list):
        if len(pokemon_list) != 5:
            raise ValueError("Incorrect number of pokemon for breeder")
        if len(list(set([pokemon.type for pokemon in pokemon_list]))) != 5:
            raise ValueError("A breeder can hold a maximum of one pokemon of each type")
        self.pokemon_list = pokemon_list

    def __str__(self):
        return str(self.pokemon_list)

    def __repr__(self):
        return self.pokemon_list

    def fight_and_give_winning_order(self, other):
        player1_pokemon = self.pokemon_list
        player2_pokemon = other.pokemon_list
        sample_space = [list(zip(x, player2_pokemon)) for x in permutations(player1_pokemon, len(player1_pokemon))]
        outcomes = [len(["win" for duel in combination if duel[0].advantage(duel[1]) == "Advantage"])
                    for combination in sample_space]
        wins = [sample_space[index] for index, outcome in enumerate(outcomes) if outcome >= 3]
        if len(wins) == 0:
            return "There are no chances of winning"
        return ";".join([str(duel[0]) for duel in wins[0]])


if __name__ == '__main__':
    print(Breeder(
        [Pokemon("Fire", 10), Pokemon("Water", 11), Pokemon("Grass", 12), Pokemon("Electric", 13),
         Pokemon("Psychic", 14)]
    ))
