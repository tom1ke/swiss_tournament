

class Match:
    """
    Classe représentant un match
    """

    def __init__(self, player_1, player_2, player_1_result=None, player_2_result=None):
        """
        Constructeur de la classe Match
        :param player_1: Joueur 1 du match, instance de Player
        :param player_2: Joueur 2 du match, instance de Player
        :param player_1_result: Résultat du joueur 1 sur ce match
                                None : remplacé par 0 ou par le résultat en base de données
        :param player_2_result: Résultat du joueur 2 sur ce match
                                None : remplacé par 0 ou par le résultat en base de données
        """
        if player_1_result is None:
            player_1_result = 0
        if player_2_result is None:
            player_2_result = 0
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_result = player_1_result
        self.player_2_result = player_2_result

    def __repr__(self):
        """
        Représentation de l'instance de match
        :return: Méthode __str__
        """
        return self.__str__()

    def __str__(self):
        """
        Représentation en chaîne de caractères de l'instance de match
        :return: Chaîne de caractères avec les données de l'instance de match
        """
        return f"{self.player_1}    {self.player_1_result} - {self.player_2_result}    {self.player_2}"

    def serialize_match(self):
        """
        Sérialisation de l'instance de match
        Les instances de joueurs sont sérialisées via la méthode __dict__
        :return: Dictionnaire pouvant être enregistré en base de données
        """
        return {
            "player_1": self.player_1.__dict__,
            "player_2": self.player_2.__dict__,
            "player_1_result": self.player_1_result,
            "player_2_result": self.player_2_result
        }
