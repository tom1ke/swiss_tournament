from util import NOW


class Round:
    def __init__(self, name, match_list=None, start_time=NOW, end_time=None, completed=False):
        if match_list is None:
            match_list = []
        if end_time is None and completed:
            end_time = NOW
        self.name = name
        self.match_list = match_list
        self.start_time = start_time
        self.end_time = end_time
        self.completed = completed

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.end_time is None:
            self.end_time = "Toujours en cours"
        return f"\n{self.name} \n" \
               f"Début : {self.start_time} \n" \
               f"Matchs : {self.match_list} \n" \
               f"Fin : {self.end_time} \n"

    def serialize_round(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "completed": self.completed
        }
