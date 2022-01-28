from datetime import datetime
from tinydb import TinyDB

"""
Database setup
"""
DB = TinyDB("data.json", indent=4)
TABLE_TOURNAMENTS = DB.table("Tournament")
TABLE_PLAYERS = DB.table("Players")
TABLE_ROUNDS = DB.table("Rounds")

"""
Tournament setup
"""
NUMBER_OF_ROUNDS = 4
NUMBER_OF_PLAYERS = 8

"""
Date & time setup
"""
NOW = datetime.now().isoformat(' ', 'seconds')

"""
Main menu options
"""
CREATE_TOURNAMENT = str(1)
GENERATE_ROUND = str(2)
ENTER_RESULTS = str(3)
LOAD_PREVIOUS_STATE = str(4)
REPORTS = str(5)
QUIT = str(6)

"""
Reports menu options
"""
ALL_ACTORS = str(1)
TOURNAMENTS = str(2)
PLAYERS = str(3)
ROUNDS = str(4)
MATCHES = str(5)
MAIN_MENU = str(6)

"""
Display mode menu options
"""
SORT_ALPHA = str(1)
SORT_RANK = str(2)
