from models import Tournament, Player

player_list = []

tournament1 = Tournament.create_tournament()
print(tournament1)

player1 = Player.create_player()
tournament1.update_player_list(player1)
print(tournament1)


