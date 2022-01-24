from views.views import View
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from util import *


class Controller:

    def __init__(self):
        self.view = View()

    def run(self):
        self.view.welcome()
        operation = self.view.input_main()

        while operation != QUIT:

            if operation == CREATE_TOURNAMENT:
                current_tournament = self.create_tournament()

                while len(current_tournament.player_list) < NUMBER_OF_PLAYERS:
                    current_player = self.add_player()
                    current_tournament.player_list.append(current_player)
                    table_players.insert(current_player.serialize_player())

                table_tournament.insert(current_tournament.serialize_tournament())

                print(current_tournament)

            elif operation == GENERATE_ROUND:
                current_tournament = self.load_tournament()

                current_tournament.player_list = self.load_players(current_tournament)
                current_tournament.round_list = self.match_players(current_tournament.player_list)

                table_rounds.insert(current_tournament.round_list)

                print(current_tournament)

            elif operation == ENTER_RESULTS:
                self.update_scores()

            elif operation == LOAD_PREVIOUS_STATE:
                current_tournament = self.load_tournament()

                current_tournament.player_list = self.load_players(current_tournament)
                current_tournament.round_list = self.load_rounds(current_tournament)

                print(current_tournament)

            operation = self.view.input_main()

        self.view.end_program()

    def create_tournament(self):
        return Tournament(*self.view.input_tournament())

    def add_player(self):
        return Player(*self.view.input_player())

    def load_tournament(self):
        return Tournament(**(table_tournament.all()[-1]))

    def load_players(self, tournament):
        players_from_db = (table_players.all()[-8:])
        for player in players_from_db:
            tournament.player_list.append(Player(**player))
        return tournament.player_list

    def load_rounds(self, tournament):
        rounds_from_db = (table_rounds.all())
        tournament.round_list.append(rounds_from_db)
        return tournament.round_list

    def sort_players(self, player_list):
        return sorted(player_list, key=lambda player: (player.score, player.ranking), reverse=True)

    def match_players(self, player_list):
        sorted_players = self.sort_players(player_list)
        upper_half = sorted_players[:len(sorted_players) // 2]
        lower_half = sorted_players[len(sorted_players) // 2:]

        return list(zip(upper_half, lower_half))

    def update_scores(self):
        self.view.enter_results()
