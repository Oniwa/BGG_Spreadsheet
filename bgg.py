from boardgamegeek import BGGClient, exceptions
BGGItemNotFoundError = exceptions.BGGItemNotFoundError


class BoardGame:
    def __init__(self):
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

    def collection_to_game(self, game):
        self.name = game.name
        self.min_players = game.minplayers
        self.max_players = game.maxplayers
        self.number_plays = game.numplays
        game = bgg.game(self.name)
        #TODO: find game by ID because Ca$h 'n Guns (Second Edition) causes an exception
        self.year = game.yearpublished

bgg = BGGClient()

# collection = bgg.collection('Brojn')
#
# for item in collection:
#     print(item.name)

# foo = bgg.collection('Oniwa', exclude_subtype='boardgameexpansion')
#
# for item in foo:
#     print(item.name)
#
# print(len(foo))
#
# class TestJunk:
#     def __init__(self):
#         self.junk = None
#
#     def foo(self, junk):
#         self.junk = junk
#
# a = [TestJunk.foo('a'), TestJunk.foo('b')]
#
# for item in a:
#     print(item.junk)

collection = bgg.collection('Oniwa', exclude_subtype='boardgameexpansion')
games = []

for item in collection:
    game = BoardGame()
    game.collection_to_game(item)
    games.append(game)

for item in games:
    print(item.year)

