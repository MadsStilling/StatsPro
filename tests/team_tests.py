import unittest
import sys
sys.path.append("../src")
import team

class TeamTests(unittest.TestCase):

    def setUp(self):
        self.dummy = team.Team()

    def test_team_exists(self):
        dummy_type = type(self.dummy)
        self.assertIs(dummy_type, team.Team)

    def test_get_team_name(self):
        self.dummy._name = "La Grande"
        self.assertEqual(self.dummy.get_team_name(), "La Grande")

    def test_set_team_name(self):
        self.dummy.set_team_name("baker city")
        self.assertEqual(self.dummy._name, "baker city")

    def test_get_team_members(self):
        self.dummy._team_members = ["Daniel", "Anna"]
        self.assertEqual(self.dummy.get_team_members(), ["Daniel", "Anna"])

    def test_add_team_member(self):
        self.dummy.add_team_members("Daniel")
        self.dummy.add_team_members("Anna", "Heather", "Kimberly")
        self.assertEqual(self.dummy.get_team_members(), ["Daniel", "Anna", "Heather", "Kimberly"])

    def test_set_opposing_team(self):
        self.dummy.set_opposing_team(1, "Bethel First")
        self.assertEqual(self.dummy._opposing_team, {1: "Bethel First"})

    def test_get_opposing_team(self):
        self.dummy.set_opposing_team(3, "Bethel First")
        self.assertEqual(self.dummy.get_opposing_team(3), "Bethel First")

    def test_add_team_round(self):
        self.dummy.add_team_round(1, 20, "Baker City", True)
        self.assertEqual(self.dummy._team_wins_losses_round, {1: "W"})
        self.assertEqual(self.dummy._team_scores[1], 20)
        self.assertEqual(self.dummy._opposing_team[1], "Baker City")

    def test_delete_team_round(self):
        self.dummy.add_team_round(2, 100, "La Grande", False)
        self.dummy.add_team_round(1, 20, "Baker City", True)
        self.dummy.remove_team_round(1)
        self.assertEqual(self.dummy._opposing_team[2], "La Grande")
        self.assertEqual(self.dummy._team_wins_losses_round, {2: "L"})
        self.assertEqual(self.dummy._team_scores[2], 100)
