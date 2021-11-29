FIFTEEN = 1
THIRTY = 2
FORTY = 3
GAME = 4

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1
    
    def score_to_output(self, score):
        if score == FIFTEEN:
            return "Fifteen"
        elif score == THIRTY:
            return "Thirty"
        elif score == FORTY:
            return "Forty"
        else:
            return "Love"
    
    def all(self):
        if self.m_score1 > FORTY:
                return "Deuce"
        else:
            return (
            self.score_to_output(self.m_score1)
            + "-All"
            )

    def past_game(self):
        score_difference = self.m_score1 - self. m_score2
        if score_difference == FIFTEEN:
            return "Advantage player1"
        elif score_difference == -FIFTEEN:
            return "Advantage player2"
        elif score_difference >= THIRTY:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_score(self):
        output = ""
        if self.m_score1 == self.m_score2:
            output = self.all()
        elif self.m_score1 >= GAME or self.m_score2 >= GAME:
            output = self.past_game()
        else:
            output = (
                self.score_to_output(self.m_score1)
                + "-"
                + self.score_to_output(self.m_score2)
            )
        return output
