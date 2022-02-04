from datetime import datetime
from tinydb import TinyDB

"""
Initialisation de la base de données TinyDB
Le fichier .json est créé à la racine du projet
Il contient une table de tournois et une table de joueurs
"""
DB = TinyDB("data.json", indent=4)
TABLE_TOURNAMENTS = DB.table("Tournament")
TABLE_PLAYERS = DB.table("Players")

"""
Caractéristiques du tournoi (nombre de tours et de joueurs)
"""
NUMBER_OF_ROUNDS = 4
NUMBER_OF_PLAYERS = 8

"""
Date & heure
"""


def get_time():
    """
    Récupère la date et l'heure actuelles
    :return: Chaîne de caractère formatée de la date et l'heure
    """
    return datetime.now().isoformat(' ', 'seconds')


"""
Variables correspondant aux options du menu principal
"""
CREATE_TOURNAMENT = "1"
GENERATE_ROUND = "2"
ENTER_RESULTS = "3"
LOAD_PREVIOUS_STATE = "4"
REPORTS = "5"
QUIT = "6"

"""
Variables correspondant aux options du menu de format de temps
"""
BLITZ = "1"
BULLET = "2"
RAPID = "3"

"""
Variables correspondant aux options du menu des rapports
"""
ALL_ACTORS = "1"
TOURNAMENTS = "2"
PLAYERS = "3"
ROUNDS = "4"
MATCHES = "5"
MAIN_MENU = "6"

"""
Variables correspondant aux options du menu de statut de tour
"""
COMPLETED = "1"
ONGOING = "2"

"""
Variables correspondant aux options du menu de classement des données des rapports
"""
SORT_ALPHA = "1"
SORT_RANK = "2"
