from models.database import DataBase
from views.views import View
from models.tournament import Tournament
from models.player import Player


class Controller:

    def __init__(self):
        self.view = View()
        self.db = DataBase("data.json", indent=4)
        self.table_tournaments = self.db.table("Tournaments")
        self.table_players = self.db.table("Players")

    def run(self):

        if self.view.input_main() == str(1):
            current_tournament = self.instantiate_tournament()
            self.table_tournaments.insert(current_tournament.serialize_tournament())

            while len(current_tournament.player_list) < 8:
                current_tournament.player_list.append(self.add_player())

            for player in current_tournament.player_list:
                self.table_players.insert(player.serialize_player())

            sorted_players = sorted(current_tournament.player_list, key=lambda player: player.ranking, reverse=True)
            upper_half = sorted_players[:len(sorted_players)//2]
            lower_half = sorted_players[len(sorted_players)//2:]

            current_tournament.round_list.append(dict(zip(upper_half, lower_half)))

            print(current_tournament)

        elif self.view.input_main() == str(2):
            pass

        else:
            self.view.end_program()

    def instantiate_tournament(self):
        return Tournament(*self.view.input_tournament())

    def add_player(self):
        return Player(*self.view.input_player())

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

