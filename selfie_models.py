from google.appengine.ext import ndb

class User(ndb.Model):
    name =  ndb.StringProperty(required=True)

class Selfie(ndb.Model):
    title =  ndb.StringProperty(required=True)
    user = ndb.KeyProperty(required=True)
    image = ndb.BlobProperty(required=True)
    price = ndb.FloatProperty(default=100.0)
