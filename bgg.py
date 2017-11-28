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

print('Name, BGG Rank, Average Rank, Personal Rank, Weight, Number Plays, Category, Mechanics, Min Players, Max Players, Suggested Players, Year Published, Purchase Date, Months Owned')
for item in foo:
    print(f'{item.name}, {item.bgg_rank}, {item.average_rating}, {item.personal_rating}, ' \
          f'{item.weight}, {item.number_plays}, {item.category}, ' \
          f'{item.mechanics}, {item.min_players}, {item.max_players}, ' \
          f'{item.suggested_players}, {item.year}, {item.bought}, ' \
          f'{item.months_owned}')
