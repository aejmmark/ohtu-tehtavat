import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        _response = requests.get(url).json()
        self.players = self.read_players(_response)

    def read_players(self, dicts):
        players = []

        for player_dict in dicts:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['nationality']
            )

            players.append(player)
        return players