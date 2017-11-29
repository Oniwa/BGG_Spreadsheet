import csv

from boardgamegeek import BGGClient, exceptions

BGGItemNotFoundError = exceptions.BGGItemNotFoundError


class BoardGame:
    def __init__(self):
        self.id = None
        self.name = None
        self.mechanics = None
        self.min_players = None
        self.max_players = None
        self.suggested_players = None
        self.bgg_rank = None
        self.year = None
        self.bought = None
        self.months_owned = None
        self.number_plays = None
        self.category = None
        self.personal_rating = None
        self.average_rating = None
        self.weight = None

    def collection_to_game(self, personal_game, db_game):
        self.name = personal_game.name
        self.min_players = personal_game.minplayers
        self.max_players = personal_game.maxplayers
        self.number_plays = personal_game.numplays
        self.id = personal_game.id
        self.personal_rating = personal_game.rating
        self.year = db_game.yearpublished
        self.weight = db_game.stats['averageweight']
        self.bgg_rank = db_game.stats['ranks'][0]['value']
        self.mechanics = ', '.join(db_game.mechanics)
        self.average_rating = db_game.stats['average']

    def csv(self):
        return [self.name, self.bgg_rank, self.average_rating, self.personal_rating,
                self.weight, self.number_plays, self.category, self.mechanics,
                self.min_players, self.max_players, self.suggested_players,
                self.year, self.bought, self.months_owned]


def csv_writer(data, path):
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            print(line)
            writer.writerow(line)


# if __name__ is "__main__":
bgg = BGGClient()

collection = bgg.collection('Oniwa', exclude_subtype='boardgameexpansion', own=True)
foo = []

game_id = []

for item in collection:
    game_id.append(item.id)

games = bgg.game_list(game_id)

for personal_game, db_game in zip(collection, games):
    game = BoardGame()
    game.collection_to_game(personal_game, db_game)
    foo.append(game)

csv_data =[]
csv_data.append('Name, BGG Rank, Average Rank, Personal Rank, Weight, '
                'Number Plays, Category, Mechanics, Min Players, Max Players, '
                'Suggested Players, Year Published, Purchase Date, '
                'Months Owned'.split(','))

for item in foo:
    csv_data.append(item.csv())

csv_writer(csv_data, './board_games.csv')
