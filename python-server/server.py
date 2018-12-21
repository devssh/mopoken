from flask import Flask, request
from game import Game
from pages import index

host = "0.0.0.0"
port = 5001

app = Flask(__name__)


@app.route("/", methods=["GET"])
def show_page():
    return index()


@app.route("/run", methods=["POST"])
def run_game():
    data = request.form
    return Game().start(data["input1"], data["input2"])


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
    # input1 = "Fire#10;Water#20;Fighting#6;Psychic#10;Electric#12"
    # input2 = "Water#10;Fighting#10;Psychic#10;Fire#12;Grass#2"
    # sample_output = "Electric#12;Fire#10;Psychic#10;Water#20;Fighting#6"
    # print(run_game(input1, input2))
