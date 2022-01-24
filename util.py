from tinydb import TinyDB

"""
Database setup
"""
db = TinyDB("data.json", indent=4)
table_tournament = db.table("Tournament")
table_players = db.table("Players")
table_rounds = db.table("Rounds")

"""
Tournament setup
"""
NUMBER_OF_ROUNDS = 4
NUMBER_OF_PLAYERS = 8

"""
Menu options
"""
CREATE_TOURNAMENT = str(1)
GENERATE_ROUND = str(2)
ENTER_RESULTS = str(3)
LOAD_PREVIOUS_STATE = str(4)
QUIT = str(5)
