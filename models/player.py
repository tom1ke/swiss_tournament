

class Player:
    def __init__(self, last_name, first_name, date_of_birth, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.date_of_birth}, {self.gender}, {self.ranking})"

    def serialize_player(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking
        }
