from util import NUMBER_OF_ROUNDS


class Tournament:

    round_total = NUMBER_OF_ROUNDS

    def __init__(self, name, location, start_date, end_date, time_control, description):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.time_control = time_control
        self.description = description
        self.round_list = []
        self.player_list = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}, " \
               f"à {self.location} en {self.round_total} tours, " \
               f"mode {self.time_control} : \n" \
               f"{self.description} \n " \
               f"Détails des tours : {self.round_list} \n " \
               f"Liste des joueurs : {self.player_list}"

    def serialize_tournament(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "time_control": self.time_control,
            "description": self.description,
            "round_total": self.round_total,
            "player_list": self.serialize_player_list()
        }

    def serialize_player_list(self):
        for player in self.player_list:
            return player.serialize_player()
