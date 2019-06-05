from google.appengine.ext import ndb

class Selfie(ndb.Model):
    title =  ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
    image = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(default=100.0)
