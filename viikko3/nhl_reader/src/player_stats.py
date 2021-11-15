class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players
        self.players.sort(key=lambda x: x.score, reverse=True)

    def top_scorers_by_nationality(self, nat):
        players_by_nat = filter(lambda x: x.nationality == nat, self.players)
        return players_by_nat