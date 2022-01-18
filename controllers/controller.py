from models.database import DataBase
from views.views import View
from models.tournament import Tournament
from models.player import Player
from util import NUMBER_OF_PLAYERS, CREATE_TOURNAMENT, LOAD_PREVIOUS_STATE, GENERATE_ROUND, QUIT


class Controller:

    def __init__(self):
        self.view = View()
        self.db = DataBase("data.json", indent=4)
        self.table_tournaments = self.db.table("Tournaments")
        self.table_players = self.db.table("Players")

    def run(self):

        operation = self.view.input_main()

        while operation != QUIT:

            if operation == CREATE_TOURNAMENT:
                current_tournament = self.instantiate_tournament()

                while len(current_tournament.player_list) < NUMBER_OF_PLAYERS:
                    current_player = self.add_player()
                    current_tournament.player_list.append(current_player)
                    self.table_players.insert(current_player.serialize_player())

                self.table_tournaments.insert(current_tournament.serialize_tournament())

                print(current_tournament)

            if operation == GENERATE_ROUND:
                current_tournament.round_list.append(self.matching_player(current_tournament.player_list))

        self.view.end_program()

    def instantiate_tournament(self):
        return Tournament(*self.view.input_tournament())

    def add_player(self):
        return Player(*self.view.input_player())

    def matching_player(self, player_list):
        sorted_players = sorted(player_list, key=lambda player: (player.score, player.ranking), reverse=True)
        upper_half = sorted_players[:len(sorted_players) // 2]
        lower_half = sorted_players[len(sorted_players) // 2:]

        return dict(zip(upper_half, lower_half))

    def load_all_data(self):
        self.db.all()

    def load_tournament(self):
        self.table_tournaments.all()

    def load_players(self):
        self.table_players.all()

    def clear_all_data(self):
        self.db.truncate()

    def clear_table_players(self):
        self.table_players.truncate()

    def clear_table_tournaments(self):
        self.table_tournaments.truncate()

