"""
Copyright (c) 2013 Daniel Seymour All rights reserved

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
        self.assertListEqual(self.dummy.get_team_members(), ["Daniel", "Anna", "Heather", "Kimberly"])