from datetime import datetime


class Round:
    def __init__(self, name, match_list=None, start_time=datetime.now(), end_time=None, completed=False):
        if match_list is None:
            match_list = []
        if end_time is None and completed:
            end_time = datetime.now()
        self.name = name
        self.match_list = match_list
        self.start_time = start_time
        self.end_time = end_time
        self.completed = completed

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.name} : \n" \
               f"Début : {self.start_time} \n" \
               f"Matchs : {self.match_list} \n" \
               f"Fin : {self.end_time}"

    def serialize_round(self):
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "completed": self.completed
        }
