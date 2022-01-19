from views.views import View
from models.tournament import Tournament
from models.player import Player
from util import *


class Controller:

    def __init__(self):
        self.view = View()

    def run(self):

        operation = self.view.input_main()

        while operation != QUIT:

            if operation == CREATE_TOURNAMENT:
                current_tournament = self.instantiate_tournament()

                while len(current_tournament.player_list) < NUMBER_OF_PLAYERS:
                    current_player = self.add_player()
                    current_tournament.player_list.append(current_player)
                    table_players.insert(current_player.serialize_player())

                table_tournament.insert(current_tournament.serialize_tournament())

                print(current_tournament)

                operation = self.view.input_main()

            if operation == GENERATE_ROUND:
                print("Rounds")
                operation = self.view.input_main()

            if operation == LOAD_PREVIOUS_STATE:
                print("Load")
                operation = self.view.input_main()

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

