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

class Team(object):

    def __init__(self):
        self._name = ""
        self._team_members = []

    """Returns the name of the team.
    Returns the name of the team.
    Returns:
        String:    The name of the team as a string.
    """
    def get_team_name(self):
        return self._name

    """Sets the name of the team.
    Simply sets the name of the team.
    Args:
        String:    The name of the team as a string.
    """
    def set_team_name(self, name):
        self._name = name

    """Gets the team_members of the team
    Gets the team members and returns a list
    Returns:
        List:    A list of all the members on a team.
    """
    def get_team_members(self):
        return self._team_members

    """Adds a team member.
    Adds an indefinite number of members to a team.
    Args:
        Any:    Will take any input type.
    """
    def add_team_members(self, *names):
        for member in names:
            self._team_members.append(member)

    """Gets the members of a team.
    Tets all of the members of the team.
    Returns:
        List:    A list of team members in any type.
    """
    def get_team_members(self):
        return self._team_members