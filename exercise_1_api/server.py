from flask import Flask
from flask import jsonify

app = Flask(__name__)

games = [
{"id": '1', 'name': 'Halo', 'year': 2001},
{"id": '2', 'name': 'Mass Effect', 'year': 2007},
{"id": '3', 'name': 'Gears of War', 'year': 2006}
]

@app.route('/games')
def games_index():
    return jsonify(games)

@app.route('/games/<games_id>')
def games_show(game_id):
    for game in games:
        if game['id'] == game_id:
            return game
    return{ "error": "Not Found" }, 404
