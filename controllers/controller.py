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
                TABLE_TOURNAMENTS.truncate()
                current_tournament = self.create_tournament()

                while len(current_tournament.player_list) < NUMBER_OF_PLAYERS:
                    current_player = self.add_player()
                    current_tournament.player_list.append(current_player)
                    TABLE_PLAYERS.insert(current_player.serialize_player())

                TABLE_TOURNAMENTS.insert(current_tournament.serialize_tournament())

                self.view.output_generic(current_tournament)

            elif operation == GENERATE_ROUND:
                last_tournament = TABLE_TOURNAMENTS.all()[-1]
                current_tournament = self.load_tournament(last_tournament)
                current_round = Round(self.view.input_round())

                current_tournament.round_list.append(current_round)

                self.match_players(current_tournament.player_list, current_round.match_list)

                current_tournament.player_list = self.sort_players(current_tournament.player_list)

                # TABLE_ROUNDS.insert(current_round.serialize_round())
                # TABLE_TOURNAMENTS.insert(current_tournament.serialize_tournament())

                self.view.output_generic(current_tournament)

            elif operation == ENTER_RESULTS:
                self.update_scores()

            elif operation == LOAD_PREVIOUS_STATE:
                last_tournament = TABLE_TOURNAMENTS.all()[-1]
                current_tournament = self.load_tournament(last_tournament)

                self.view.output_generic(current_tournament)

            elif operation == REPORTS:
                report_op = self.view.input_reports()

                while report_op != MAIN_MENU:

                    if report_op == ALL_ACTORS:
                        player_list = []
                        for player in TABLE_PLAYERS.all():
                            current_player = Player(**player)
                            player_list.append(current_player)
                        for index, player in enumerate(player_list, start=1):
                            self.view.output_indexed(index, player)

                    elif report_op == TOURNAMENTS:
                        tournament_list = []
                        for tournament in TABLE_TOURNAMENTS.all():
                            current_tournament = self.load_tournament(tournament)
                            tournament_list.append(current_tournament)
                        for index, tournament in enumerate(tournament_list, start=1):
                            self.view.output_indexed(index, tournament)

                    elif report_op == PLAYERS:
                        pass

                    elif report_op == ROUNDS:
                        pass

                    elif report_op == MATCHES:
                        pass

                    report_op = self.view.input_reports()

            operation = self.view.input_main()

        self.view.end_program()

    def create_tournament(self):
        return Tournament(*self.view.input_tournament())

    def add_player(self):
        return Player(*self.view.input_player())

    def load_tournament(self, db_tournament):
        loaded_tournament = Tournament(**db_tournament)

        loaded_players = [Player(**player) for player in loaded_tournament.player_list]
        loaded_tournament.player_list.clear()
        for player in loaded_players:
            loaded_tournament.player_list.append(player)

        loaded_rounds = [Round(**round_) for round_ in loaded_tournament.round_list]
        loaded_tournament.round_list.clear()
        for round_ in loaded_rounds:
            loaded_tournament.round_list.append(round_)

            loaded_matches = [Match(**match_) for match_ in round_.match_list]
            round_.match_list.clear()
            for match_ in loaded_matches:
                round_.match_list.append(match_)

        return loaded_tournament

    def load_players_from_db(self, tournament):
        loaded_players = [Player(**player) for player in tournament.player_list]
        tournament.player_list.clear()
        for player in loaded_players:
            tournament.player_list.append(player)
        return tournament.player_list

    def load_rounds(self, tournament):
        rounds_from_db = (TABLE_ROUNDS.all())
        tournament.round_list.append(rounds_from_db)
        return tournament.round_list

    def sort_players(self, player_list):
        return sorted(player_list, key=lambda player: (player.score, player.ranking), reverse=True)

    def match_players(self, player_list, match_list):
        sorted_players = self.sort_players(player_list)
        upper_half = sorted_players[:len(sorted_players) // 2]
        lower_half = sorted_players[len(sorted_players) // 2:]

        for player_1, player_2 in zip(upper_half, lower_half):
            pair = Match(player_1, player_2)
            match_list.append(pair)
        return match_list

    def update_scores(self):
        self.view.enter_results()
