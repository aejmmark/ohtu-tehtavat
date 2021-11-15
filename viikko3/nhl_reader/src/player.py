class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.score = self.assists + self.goals
    
    def __str__(self):
        return  (f"{self.name:30}" +  f"{self.team:4}"
        + f"{self.goals:2}" + " + " + f"{self.assists:2}"
        + " = " + str(self.score))
