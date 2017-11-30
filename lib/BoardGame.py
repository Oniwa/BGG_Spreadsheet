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

