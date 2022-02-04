from util import get_time


class Round:
    """
    Classe représentant un tour
    """

    def __init__(self, name, match_list=None, start_time=None, end_time=None, completed=None):
        """
        Constructeur de la classe Round
        :param name: Nom du tour
        :param match_list: Liste des matchs
                           None : remplacé par une liste vide ou la liste des matchs du tour en base de données
        :param start_time: Date et heure de début
                           None : remplacé par date + heure de création (via fonction util.get_time)
                           ou date + heure en base données
        :param end_time: Date et heure de fin
                         None : remplacé par date + heure si le tour est clôturé par l'utilisateur (via param
                         "Completed")
                         ou date + heure en base de données
        :param completed: État du tour (en cours/fini)
                          False par défaut, passe à True via choix utilisateur
        """
        if match_list is None:
            match_list = []
        if start_time is None:
            start_time = get_time()
        if end_time is None and completed:
            end_time = get_time()
        if completed is None:
            completed = False
        self.name = name
        self.match_list = match_list
        self.start_time = start_time
        self.end_time = end_time
        self.completed = completed

    def __repr__(self):
        """
        Représentation de l'instance de tour
        :return: Méthode __str__
        """
        return self.__str__()

    def __str__(self):
        """
        Représentation en chaîne de caractères de l'instance de tour
        Variable nl pour retour à la ligne dans les f' strings
        :return: Chaîne de caractère avec les données de l'instance de tour
        """
        nl = "\n"
        if self.end_time is None:
            self.end_time = "Toujours en cours"
        return f"\n{self.name} \n" \
               f"Début : {self.start_time} \n" \
               f"Matchs : \n{(nl.join(map(str, self.match_list)))} \n" \
               f"Fin : {self.end_time} \n"

    def serialize_round(self):
        """
        Sérialisation de l'instance de tour
        La liste des matchs est sérialisée par la méthode serialize_match_list
        :return: Dictionnaire pouvant être enregistré en base de données
        """
        return {
            "name": self.name,
            "match_list": self.serialize_match_list(),
            "start_time": self.start_time,
            "end_time": self.end_time,
            "completed": self.completed
        }

    def serialize_match_list(self):
        """
        Sérialisation de la liste des matchs de l'instance de tour
        :return: Liste de matchs sérialisés pour chaque match dans la "match_list"
        """
        return [matches.serialize_match() for matches in self.match_list]
