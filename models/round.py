from util import get_time


class Round:
    def __init__(self, name, match_list=None, start_time=None, end_time=None, completed=None):
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
        return self.__str__()

    def __str__(self):
        nl = "\n"
        if self.end_time is None:
            self.end_time = "Toujours en cours"
        return f"\n{self.name} \n" \
               f"Début : {self.start_time} \n" \
               f"Matchs : \n{(nl.join(map(str, self.match_list)))} \n" \
               f"Fin : {self.end_time} \n"

    def serialize_round(self):
        return {
            "name": self.name,
            "match_list": self.serialize_match_list(),
            "start_time": self.start_time,
            "end_time": self.end_time,
            "completed": self.completed
        }

    def serialize_match_list(self):
        return [matches.serialize_match() for matches in self.match_list]
