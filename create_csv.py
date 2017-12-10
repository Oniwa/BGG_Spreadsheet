import csv
import os

from boardgamegeek import BGGClient

from lib import BoardGame


def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)

bgg = BGGClient()

collection = bgg.collection('Oniwa', exclude_subtype='boardgameexpansion', own=True)
foo = []

game_id = []

for item in collection:
    game_id.append(item.id)

games = bgg.game_list(game_id)

for personal_game, db_game in zip(collection, games):
    game = BoardGame.BoardGame()
    game.collection_to_game(personal_game, db_game)
    foo.append(game)

# TODO: Change Average rank and personal rank to rating and add a personal rank field
csv_data = [['Name', 'BGG Rank', 'Average Rank', 'Personal Rank', 'Weight',
            'Number Plays', 'Category', 'Mechanics', 'Min Players',
            'Max Players', 'Suggested Players', 'Year Published',
            'Purchase Date', 'Months Owned']]

for item in foo:
    csv_data.append(item.csv())

print(csv_data)
cwd = os.getcwd()
data_dir = cwd + '\\data\\board_games.csv'

csv_writer(csv_data, data_dir)
