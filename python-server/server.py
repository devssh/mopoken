from flask import Flask, request, jsonify
import json

host = "0.0.0.0"
port = 5001

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
  return "Hello World"


if __name__ == '__main__':
  app.run(host=host, port=port, debug=True)
