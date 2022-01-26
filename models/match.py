

class Match:

    def __init__(self, player_1, player_2, player_1_result=None, player_2_result=None):
        if player_1_result is None:
            player_1_result = 0
        if player_2_result is None:
            player_2_result = 0
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_result = player_1_result
        self.player_2_result = player_2_result
        self.player_pair = ([self.player_1, self.player_1_result], [self.player_2, self.player_2_result])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.player_1}    {self.player_1_result} - {self.player_2_result}    {self.player_2}"

    def serialize_match(self):
        return {
            "player_1": self.player_1.__dict__,
            "player_2": self.player_2.__dict__,
            "player_1_result": self.player_1_result,
            "player_2_result": self.player_2_result
        }
