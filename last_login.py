#!/usr/bin/env python

from pymongo import MongoClient
import pprint
import json

client = MongoClient()
db = client.wakari

users = db.users

def list_last_active_users():
    for coll_document in users.find():
        name = coll_document.get('username')
        time = coll_document.get('time')
        last_seen = time.get('last_seen')
        print('user: ' + name + ' was last seen on ' +  last_seen)


list_last_active_users()
