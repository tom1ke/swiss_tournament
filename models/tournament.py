from util import NUMBER_OF_ROUNDS, BLITZ, BULLET, RAPID


class Tournament:
    """
    Classe pour créer une instance de tournoi
    """

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
        """
        Constructeur de la classe Tournament
        :param name: Nom du tournoi
        :param location: Lieu du tournoi
        :param start_date: Date de début du tournoi
        :param end_date: Date de fin du tournoi
        :param description: Description du tournoi
        :param time_control: Format de temps des matchs
                             None : remplacé par le choix utilisateur ou le format enregistré en base de données
        :param round_total: Nombre de tours du tournoi, défini dans la variable util.NUMBER_OF_ROUNDS
        :param round_list: Liste des tours
                           None : remplacé par une liste vide ou liste des tours en base de données
        :param player_list: Liste des joueurs
                            None : remplacé par une liste vide ou liste des joueurs en base données
        """
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
        """
        Représention de l'instance de tournoi
        :return: Méthode __str__
        """
        return self.__str__()

    def __str__(self):
        """
        Représentation en chaîne de caractères de l'instance de tournoi
        Variable nl pour retour à la ligne dans les f' strings
        :return: Chaîne de caractère avec les données de l'instance de tournoi
        """
        nl = "\n"
        return f"\n{self.name}, du {self.start_date} au {self.end_date}, " \
               f"à {self.location} en {self.round_total} tours, " \
               f"mode {self.time_control} :\n" \
               f"{self.description}\n" \
               f"Détails des tours : \n{(nl.join(map(str, self.round_list)))}\n" \
               f"Liste des joueurs : \n{(nl.join(map(str, self.player_list)))}"

    def serialize_tournament(self):
        """
        Sérialialisation de l'instance de tournoi
        La liste des tours et des joueurs sont sérialisées par les méthodes
        - serialize_round_list
        - serialize_player_list
        :return: Dictionnaire pouvant être enregistré en base de données
        """
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
        """
        Sérialisation de la liste des tours de l'instance de tournoi
        :return: Liste de tours sérialisés pour chaque tour dans la "round_list"
        """
        return [rounds.serialize_round() for rounds in self.round_list]

    def serialize_player_list(self):
        """
         Sérialisation de la liste des joueurs de l'instance de tournoi
        :return: Liste de joueurs sérialisés pour chaque instance de joueur dans la "player_list"
        """
        return [player.__dict__ for player in self.player_list]
