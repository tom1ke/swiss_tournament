from models import Tournament, Player

player_list = []

tournament1 = Tournament.create_tournament()
print(tournament1)

player1 = Player.create_player()
print(player1)
player_list.append(player1)
