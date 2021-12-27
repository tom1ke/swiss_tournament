from views.views import View
from models.tournament import Tournament
from models.player import Player


class Controller:

    def __init__(self):
        self.view = View()

    def run(self):

        if self.view.input_main() == str(1):
            current_tournament = self.instantiate_tournament()
            while len(current_tournament.player_list) < 8:
                current_tournament.player_list.append(self.add_players())
            print(current_tournament.player_list)
        else:
            self.view.end_program()

    def instantiate_tournament(self):

        t = self.view.input_tournament()

        return Tournament(t[0], t[1], t[2], t[3], t[4], t[5])

    def add_players(self):

        p = self.view.input_player()

        return Player(p[0], p[1], p[2], p[3], p[4])
