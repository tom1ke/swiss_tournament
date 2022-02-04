

class Player:
    """
    Classe représentant un joueur
    """

    def __init__(self, last_name, first_name, date_of_birth, gender, ranking, score=0, index=None):
        """
        Constructeur de la classe Player
        :param last_name: Nom de famille
        :param first_name: Prénom
        :param date_of_birth: Date de naissance
        :param gender: Sexe
        :param ranking: Classement/ELO du joueur
        :param score: Score du joueur dans le tournoi, par défaut 0
        :param index: Position du joueur dans la liste du tournoi
                      None : remplacé par l'index de l'ordre de création ou l'index en base de données
        """
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.index = index

    def __repr__(self):
        """
        Représentation de l'instance de joueur
        :return: Méthode __str__
        """
        return self.__str__()

    def __str__(self):
        """
        Représentation en chaîne de caractère de l'instance de joueur
        :return: Chaîne de caractères avec les données de l'instance de joueur
        """
        return f"{self.last_name} " \
               f"{self.first_name} " \
               f"({self.date_of_birth}, {self.gender}, {self.ranking}, {self.score})"

    def serialize_player(self):
        """
        Sérialisation de l'instance de joueur
        :return: Dictionnaire (via méthode __dict__) pouvant être enregistré en base données
        """
        return self.__dict__
