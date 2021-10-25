from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

games = [
{"id": '1', 'name': 'Halo', 'year': 2001},
{"id": '2', 'name': 'Mass Effect', 'year': 2007},
{"id": '3', 'name': 'Gears of War', 'year': 2006}
]


@app.route('/games')
def games_index():
  return(render_template('/templates/index.html'))

@app.route('/games/<games_id>')
def games_show(games_id):
    for game in games:
        if game['id'] == games_id:
            return game
    return{ "error": "Not Found" }, 404

@app.route('/movies', methods=['POST'])
def games_create():
    new_game = request.get_json()
    new_game['id'] = str(len(games) + 1 )
    games.append(new_game)
    return{ 'message': 'Game created successfully' }, 201

@app.route('/games/<game_id>', methods=['PATCH'])
def games_update(game_id):
    updates = request.get_json()

    for game in games:
        if game['id'] == game_id:
            game.update(updates)
            return { 'message': 'Game was updated successfully' }, 201

@app.route('/games/<game_id>', methods=['DELETE'])
def games_delete(game_id):
    found_game_idx = None

    for i in range(len(games)): # 0, 1, 2
      if games[i]['id'] == game_id:
        found_game_idx = i
        break
  
    if found_game_idx != None:
      games.pop(found_game_idx)
      return { 'message': 'Game deleted successfully' }, 201

    return { 'error': 'Not Found' }, 404


app.run()