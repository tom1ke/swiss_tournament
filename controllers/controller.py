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

        self.run_main_menu()

        self.view.end_program()

    def run_main_menu(self):
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

                current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)

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
                self.run_reports_menu()

            else:
                self.view.invalid_choice()

            operation = self.view.input_main()

    def run_reports_menu(self):
        report_op = self.view.input_reports()

        while report_op != MAIN_MENU:

            if report_op == ALL_ACTORS:
                player_list = self.display_mode(self.load_players_from_db())
                for index, player in enumerate(player_list, start=1):
                    self.view.output_indexed(index, player)

            elif report_op == TOURNAMENTS:
                tournament_list = self.load_tournaments_from_db()
                for index, tournament in enumerate(tournament_list, start=1):
                    self.view.output_indexed(index, tournament)

            elif report_op == PLAYERS:
                selected_tournament = self.select_tournament_from_db()
                self.indexing_output(selected_tournament.player_list)

            elif report_op == ROUNDS:
                selected_tournament = self.select_tournament_from_db()
                self.indexing_output(selected_tournament.round_list)

            elif report_op == MATCHES:
                selected_tournament = self.select_tournament_from_db()
                all_match_lists = [round_.match_list for round_ in selected_tournament.round_list]
                self.indexing_output(list(*all_match_lists))

            else:
                self.view.invalid_choice()

            report_op = self.view.input_reports()

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
                match_.player_1 = Player(**match_.player_1)
                match_.player_2 = Player(**match_.player_2)
                round_.match_list.append(match_)

        return loaded_tournament

    def load_tournaments_from_db(self):
        tournament_list = []
        for tournament in TABLE_TOURNAMENTS.all():
            loaded_tournament = self.load_tournament(tournament)
            tournament_list.append(loaded_tournament)
        return tournament_list

    def select_tournament_from_db(self):
        tournament_list = self.load_tournaments_from_db()
        tournament_index = (int(self.view.input_reports_tournament_choice()) - 1)
        if 0 <= tournament_index < len(tournament_list):
            return self.load_tournament(TABLE_TOURNAMENTS.all()[tournament_index])
        else:
            return self.view.invalid_choice()

    def load_players_from_db(self):
        player_list = []
        for player in TABLE_PLAYERS.all():
            loaded_player = Player(**player)
            player_list.append(loaded_player)
        return player_list

    def load_rounds_by_tournaments(self, tournament):
        pass

    def load_matches_by_tournaments(self, tournament):
        pass

    def sort_players_by_rank(self, player_list):
        return sorted(player_list, key=lambda player: (player.score, player.ranking), reverse=True)

    def sort_players_by_name(self, player_list):
        return sorted(player_list, key=lambda player: (player.last_name, player.first_name))

    def match_players(self, player_list, match_list):
        sorted_players = self.sort_players_by_rank(player_list)
        upper_half = sorted_players[:len(sorted_players) // 2]
        lower_half = sorted_players[len(sorted_players) // 2:]

        for player_1, player_2 in zip(upper_half, lower_half):
            pair = Match(player_1, player_2)
            match_list.append(pair)
        return match_list

    def update_scores(self):
        self.view.enter_results()

    def display_mode(self, list_to_sort):
        display_mode = self.view.input_display_mode()
        if display_mode == SORT_ALPHA:
            list_to_sort = self.sort_players_by_name(list_to_sort)
        elif display_mode == SORT_RANK:
            list_to_sort = self.sort_players_by_rank(list_to_sort)
        else:
            self.view.invalid_choice()
        return list_to_sort

    def indexing_output(self, obj_list):
        return [self.view.output_indexed(index, obj) for index, obj in enumerate(obj_list, start=1)]
