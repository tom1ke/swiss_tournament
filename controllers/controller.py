from itertools import chain, cycle, combinations
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
                current_tournament = self.create_tournament()

                player_index = 0
                while len(current_tournament.player_list) < NUMBER_OF_PLAYERS:
                    player_index += 1
                    current_player = self.add_player()
                    current_player.index = player_index
                    current_tournament.player_list.append(current_player)
                    TABLE_PLAYERS.insert(current_player.serialize_player())

                TABLE_TOURNAMENTS.insert(current_tournament.serialize_tournament())

                self.view.output_generic(current_tournament)

            elif operation == GENERATE_ROUND:
                try:
                    last_tournament = TABLE_TOURNAMENTS.all()[-1]
                    current_tournament = self.load_tournament(last_tournament)
                    if len(current_tournament.round_list) >= NUMBER_OF_ROUNDS:
                        self.view.output_max_round()
                    else:
                        current_round = Round(self.view.input_round())
                        current_tournament.round_list.append(current_round)
                        current_round.match_list = self.match_players(current_tournament)
                        current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)

                        TABLE_TOURNAMENTS.update(current_tournament.serialize_tournament(),
                                                 doc_ids=[last_tournament.doc_id])

                        self.view.output_generic(current_tournament)

                except IndexError:
                    raise IndexError
                    # self.view.no_data()

            elif operation == ENTER_RESULTS:
                try:
                    last_tournament = TABLE_TOURNAMENTS.all()[-1]
                    current_tournament = self.load_tournament(last_tournament)
                    current_round = current_tournament.round_list[-1]
                    if current_round.completed:
                        self.view.output_results_done()
                    else:
                        self.update_scores(current_round, current_tournament)
                        self.complete_round(current_round)
                        current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)

                        TABLE_TOURNAMENTS.update(current_tournament.serialize_tournament(),
                                                 doc_ids=[last_tournament.doc_id])

                        self.view.output_generic(current_tournament)

                except IndexError:
                    self.view.no_data()

            elif operation == LOAD_PREVIOUS_STATE:
                try:
                    last_tournament = TABLE_TOURNAMENTS.all()[-1]
                    current_tournament = self.load_tournament(last_tournament)
                    current_tournament.player_list = self.sort_players_by_rank(current_tournament.player_list)
                    self.view.output_generic(current_tournament)

                except IndexError:
                    self.view.no_data()

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
                self.indexing_output(player_list)

                if len(player_list) == 0:
                    self.view.no_data()

            elif report_op == TOURNAMENTS:
                tournament_list = self.load_tournaments_from_db()
                self.indexing_output(tournament_list)

                if len(tournament_list) == 0:
                    self.view.no_data()

            elif report_op == PLAYERS:
                try:
                    selected_tournament = self.select_tournament_from_db()
                    self.indexing_output(selected_tournament.player_list)

                except AttributeError:
                    self.view.no_data()

            elif report_op == ROUNDS:
                try:
                    selected_tournament = self.select_tournament_from_db()
                    self.indexing_output(selected_tournament.round_list)

                except AttributeError:
                    self.view.no_data()

            elif report_op == MATCHES:
                try:
                    selected_tournament = self.select_tournament_from_db()
                    all_match_lists = [round_.match_list for round_ in selected_tournament.round_list]
                    self.indexing_output(chain(*all_match_lists))

                except AttributeError:
                    self.view.no_data()

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

    def sort_players_by_rank(self, player_list):
        return sorted(player_list, key=lambda player: (player.score, player.ranking), reverse=True)

    def sort_players_by_name(self, player_list):
        return sorted(player_list, key=lambda player: (player.last_name, player.first_name))

    def match_players(self, tournament):
        round_match_list = []
        sorted_players = self.sort_players_by_rank(tournament.player_list)

        if len(tournament.round_list) == 1:
            half_number_of_players = len(sorted_players) // 2

            for i in range(half_number_of_players):
                player_1 = sorted_players[i]
                player_2 = sorted_players[i+half_number_of_players]
                pair = Match(player_1, player_2)
                round_match_list.append(pair)

        elif len(tournament.round_list) > 1:
            played_matches = self.check_played_matches()
            used_players = []

            for i in range(len(sorted_players)):
                if i % 2 == 0:
                    player_1 = sorted_players[i]
                    player_2 = sorted_players[i+1]

                    used_players.extend([player_1.index, player_2.index])

                    for match_ in played_matches:
                        while match_.player_1.index in [
                            player_1.index,
                            player_2.index,
                        ] and match_.player_2.index in [player_1.index, player_2.index]:
                            if len(round_match_list) < 3:
                                player_2 = sorted_players[i+2]
                            else:
                                player_2 = sorted_players[i-1]

                    pair = Match(player_1, player_2)
                    round_match_list.append(pair)

        return round_match_list

    def check_played_matches(self):
        last_tournament = TABLE_TOURNAMENTS.all()[-1]
        current_tournament = self.load_tournament(last_tournament)
        all_match_lists = [round_.match_list for round_ in current_tournament.round_list]
        return list(chain(*all_match_lists))

    def update_scores(self, round_, tournament):
        for match_ in round_.match_list:
            results = (self.view.input_results(match_))
            match_.player_1_result = float(results[0])
            match_.player_2_result = float(results[1])

            for player in tournament.player_list:
                if player.index == match_.player_1.index:
                    player.score = player.score + match_.player_1_result
                elif player.index == match_.player_2.index:
                    player.score = player.score + match_.player_2_result

    def complete_round(self, round_):
        round_state = self.view.input_completed_round()
        if round_state == COMPLETED:
            round_.completed = True

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
