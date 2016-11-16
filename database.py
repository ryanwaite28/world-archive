# --- --- -- --- --- --- #
# --- Import Modules --- #
# --- --- -- --- --- --- #

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

from ming import create_datastore
from ming.odm import ThreadLocalODMSession
from ming import schema
from ming.odm import MappedClass
from ming.odm import FieldProperty, ForeignIdProperty

session = ThreadLocalODMSession(
    bind = create_datastore('mongodb://localhost:27017')
)

db = session.db

collections = {
    'users': db.users,
    'people': db.people
}
