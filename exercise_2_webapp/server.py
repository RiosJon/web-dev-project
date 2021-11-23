import csv
from flask import Flask, request, render_template

DATA_FILE = 'data.csv'
FIELDNAMES = ['id', 'name', 'year', 'summary']

app = Flask(__name__)

games = []

def load_data_file():
  with open(DATA_FILE) as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
      games.append(row)

def append_data_file(new_row):
  with open(DATA_FILE, 'a', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
    writer.writerow(new_row)

@app.route('/games')
def games_index():
  return(render_template('/index.html',games=games))

@app.route('/games/<games_id>')
def games_show(games_id):
    for game in games:
        if game['id'] == games_id:
            return render_template('index.html', games=games)
   
    return{ "error": "Not Found" }, 404

@app.route('/movies', methods=['POST'])
def games_create():
    new_game = request.get_json()
    new_game['id'] = str(len(games) + 1 )
    games.append(new_game)
    append_data_file(new_game)
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

load_data_file()
app.run()