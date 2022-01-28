

class Player:
    def __init__(self, last_name, first_name, date_of_birth, gender, ranking, score=0, index=None):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.index = index

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.last_name} " \
               f"{self.first_name} " \
               f"({self.date_of_birth}, {self.gender}, {self.ranking}, {self.score})"

    def serialize_player(self):
        return self.__dict__
