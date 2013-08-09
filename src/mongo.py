"""
Copyright (c) 2013 William Fleming All rights reserved

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

"""Class for connecting to the mongodb. 

- Allows for inputting of rounds and players into a scalable mongodb database
- Allows for searching for rounds and persons
"""
import pymongo
import datetime
from pymongo import MongoClient

class pymongodb(object):
	
	def __init__(self):
		
		self.person  = {}
		self.round   = {}
		self.team    = {}
		self.members = {}

	def connect_to_mongo():
	    
	    client = MongoClient("localhost", 27017)
	    db = client.statpro

	def post_person(self, _round, _person):
			post = {"person": self.person[_person],
        			"round" : self.round[_round],
        			"date"  : datetime.datetime.today()}
			person = db.person
			person_id = person.insert(person)

	def post_round(self, _team, _members):
			post = {"team"    : self.team[_team],
        			"members" : self.members[_members],
        			"date"    : datetime.datetime.today()}

			round = db.round
			round_id = round.insert(round)

	def search_person():
		person.find_one({"_id": person_pers})

	def search_round():
		round.find_one({"_id": round_rond})


