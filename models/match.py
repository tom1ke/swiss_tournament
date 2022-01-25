

class Match:

    def __init__(self, player_1=None, player_2=None, player_1_result=0, player_2_result=0):
        if player_1 is None:
            player_1 = []
        if player_2 is None:
            player_2 = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_result = player_1_result
        self.player_2_result = player_2_result
        self.player_pair = ([self.player_1, self.player_1_result], [self.player_2, self.player_2_result])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.player_1} ({self.player_1_result}) contre {self.player_2} ({self.player_2_result})"
