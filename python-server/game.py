from match import Match
from breeder import breeder_types, Breeder
from parser import Parser


class Game:

    def start(self, input1, input2):
        breeder1 = Breeder('player', Parser(input1).pokemon_list)
        breeder2 = Breeder('npc', Parser(input2).pokemon_list)

        results = Match(breeder1, breeder2).results()
        victor = results[0]
        order = results[1]
        if ((breeder1.type == breeder_types[1]) and (victor == breeder1)) or (
                (breeder2.type == breeder_types[1]) and (victor == breeder2)):
            return "The winning order for player is " + ";".join([str(pokemon) for pokemon in order])
        else:
            if (breeder1.type != breeder_types[1]) and (breeder2.type != breeder_types[1]):
                return "Invalid game between npc"
            else:
                return "There are no chances of winning"


if __name__ == '__main__':
    input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
    input2 = "Water#10;Fighting#10;Psychic#100;Fire#12;Grass#2"
    print(Game().start(input1, input2))
