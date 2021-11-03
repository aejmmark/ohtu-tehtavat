import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_finds_name(self):
        self.assertIsNotNone(self.statistics.search("Semenko"))

    def test_failed_search_returns_none(self):
        self.assertIsNone(self.statistics.search("Bob"))
    
    def test_team_returns_correct_players(self):
        players_of_team = self.statistics.team("EDM")
        self.assertTrue(
            players_of_team[0].team == "EDM" and
            players_of_team[1].team == "EDM" and
            players_of_team[2].team == "EDM"
        )
    
    def test_wrong_team_returns_empty_list(self):
        players_of_team = self.statistics.team("Bob")
        self.assertTrue(0 == len(players_of_team))

    def test_top_scorers_returns_correct_number_of_players(self):
        scorers = self.statistics.top_scorers(3)
        self.assertTrue(4 == len(scorers))

    def test_top_scorers_first_has_highest_score(self):
        scorers = self.statistics.top_scorers(3)
        self.assertTrue(scorers[0].points > scorers[3].points)
