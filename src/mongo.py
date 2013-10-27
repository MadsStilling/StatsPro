"""Class for connecting to the mongodb.

- Allows for inputting of rounds and players into a scalable mongodb database
- Allows for searching for rounds and persons
"""
import pymongo
import datetime
from pymongo import MongoClient

<<<<<<< HEAD
class MongoDB(object):
    def __init__(self):
    	self.database
        self.person
        self.round_
        self.date = datetime.date.today()

    def connect_to_mongo_database(self):
        client = MongoClient("localhost", 27017)
        self.database = client.StatsPro

    def initial_post_person(self, person, round_):
        post = {"person"  : person,
                "round"   : round_,
                "date"    : datetime.date.today()
                }
        self.person = database.person
        person_pers = person.insert(person)

    def initial_post_team(self, team, round_):
        post = {"team"    : team,
                "members" : members,
                "date"    : datetime.date.today()
                }
        self.round_ = database.round_
        round_rond = self.round_.insert(round_)

    def search_person(self, name):
        person.find_one({"person": name})

    def search_round(self, number):
        round_.find_one({"round": number})
=======
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


>>>>>>> 44688ad20b3d5d6640501853e0b285dd6edcc829
