from pokemon import Pokemon


class Parser:
    def __init__(self, input_text):
        if (";" not in input_text) or ("#" not in input_text):
            raise ValueError("Incorrect input string")
        if len(input_text.split(";")) != 5:
            raise ValueError("Incorrect number of pokemon")
        if len([pokemon for pokemon in input_text.split(";") if "#" in pokemon]) != 5:
            raise ValueError("Incorrect format for pokemon")
        try:
            pokemon_list = [Pokemon(*pokemon.split("#")) for pokemon in input_text.split(";")]
            self.pokemon_list = pokemon_list
        except Exception:
            raise ValueError("Error in input string")


if __name__ == '__main__':
    print(Parser("Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12").pokemon_list)
