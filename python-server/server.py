from flask import Flask, request, jsonify
import json
from pokemon import Pokemon

host = "0.0.0.0"
port = 5001

app = Flask(__name__)

input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
output = "Electric#12;Fire#10;Psychic#10;Water#20;Fighting#6"



@app.route("/", methods=["GET", "POST"])
def hello():
    player1_pokemon = [Pokemon(*pokemon.split("#")) for pokemon in input1.split(";")]
    player2_pokemon = [Pokemon(*pokemon.split("#")) for pokemon in input2.split(";")]
    return


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
