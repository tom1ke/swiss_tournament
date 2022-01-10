from views.views import View
from models.tournament import Tournament
from models.player import Player


class Controller:

    def __init__(self):
        self.view = View()

    def run(self):

        if self.view.input_main() == str(1):
            current_tournament = self.instantiate_tournament()
            current_tournament.serialize_tournament()

            while len(current_tournament.player_list) < 8:
                current_tournament.player_list.append(self.add_players())

            sorted(current_tournament.player_list, key=lambda player: player.ranking, reverse=True)
            print(*current_tournament.player_list)

        else:
            self.view.end_program()

    def instantiate_tournament(self):

        return Tournament(*self.view.input_tournament())

    def add_players(self):

        return Player(*self.view.input_player())
