

class Player:
    def __init__(self, last_name, first_name, date_of_birth, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

    def __repr__(self):
        return f"{self.last_name} {self.first_name} ({self.date_of_birth}, {self.gender}, {self.ranking})"

    @classmethod
    def create_player(cls):
        return cls(
            last_name=input("Nom de famille : "),
            first_name=input("Prénom : "),
            date_of_birth=input("Date de naissance JJ/MM/AAA : "),
            gender=input("Sexe : "),
            ranking=input("Classement : ")
        )
