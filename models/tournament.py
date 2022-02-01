from util import NUMBER_OF_ROUNDS, BLITZ, BULLET, RAPID


class Tournament:

    def __init__(self,
                 name,
                 location,
                 start_date,
                 end_date,
                 description,
                 time_control=None,
                 round_total=NUMBER_OF_ROUNDS,
                 round_list=None,
                 player_list=None):
        if time_control == BLITZ:
            time_control = "Blitz"
        if time_control == BULLET:
            time_control = "Bullet"
        if time_control == RAPID:
            time_control = "Coup rapide"
        if round_list is None:
            round_list = []
        if player_list is None:
            player_list = []
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.round_total = round_total
        self.round_list = round_list
        self.player_list = player_list

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        nl = "\n"
        return f"\n{self.name}, du {self.start_date} au {self.end_date}, " \
               f"à {self.location} en {self.round_total} tours, " \
               f"mode {self.time_control} :\n" \
               f"{self.description}\n" \
               f"Détails des tours : \n{(nl.join(map(str, self.round_list)))}\n" \
               f"Liste des joueurs : \n{(nl.join(map(str, self.player_list)))}"

    def serialize_tournament(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "round_total": self.round_total,
            "round_list": self.serialize_round_list(),
            "player_list": self.serialize_player_list()
        }

    def serialize_round_list(self):
        return [rounds.serialize_round() for rounds in self.round_list]

    def serialize_player_list(self):
        return [player.__dict__ for player in self.player_list]
