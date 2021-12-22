

class Tournament:
    def __init__(self, name, location, date, round_total, round_list, player_list, time_control, description):
        self.name = name
        self.location = location
        self.date = date
        self.round_total = round_total
        self.round_list = round_list
        self.player_list = player_list
        self.time_control = time_control
        self.description = description

    def __repr__(self):
        return f"Tournoi {self.name} du {self.date} à {self.location} en {self.round_total} tours, " \
               f"mode {self.time_control} \n" \
               f"{self.description} \n " \
               f"Détails des tours : {self.round_list} \n " \
               f"Liste des joueurs : {self.player_list}"

    @classmethod
    def create_tournament(cls):
        return cls(
            name=input("Nom du tournoi : "),
            location=input("Lieu du tournoi : "),
            date=input("Date du tournoi (JJ/MM/AA) : "),
            round_total=str(4),
            round_list=[],
            player_list=[],
            time_control=input("Bullet, Blitz ou Coup rapide : "),
            description=input("Description du tournoi : ")
        )

    def update_player_list(self, player_instance):
        self.player_list.append(player_instance)

    def update_round_list(self, round_instance):
        self.round_list.append(round_instance)

    def save_tournament(self):
        pass
