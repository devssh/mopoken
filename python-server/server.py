from flask import Flask, request, jsonify
from breeder import Breeder
from parser import Parser

host = "0.0.0.0"
port = 5001

app = Flask(__name__)

input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
output = "Electric#12;Fire#10;Psychic#10;Water#20;Fighting#6"


@app.route("/", methods=["GET", "POST"])
def hello():
    player1 = Breeder(Parser(input1).pokemon_list)
    player2 = Breeder(Parser(input2).pokemon_list)

    return player1.fight_and_give_winning_order(player2)


if __name__ == '__main__':
    # app.run(host=host, port=port, debug=True)
    print(hello())
