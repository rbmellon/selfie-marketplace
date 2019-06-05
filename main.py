# the import section
import webapp2
import jinja2
import os

import seed_db
from selfie_models import Selfie

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class HomePage(webapp2.RequestHandler):
    def get(self): #for a get request
        selfies = Selfie.query().fetch()
        template = env.get_template("templates/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render({'selfies' : selfies}))

# the handler section
class UploadPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        template = env.get_template("templates/upload.html")
        self.response.write(template.render()) #the response

    def post(self): #for a get request
        contents = {
          'title': self.request.get("title"),
          'image': self.request.get("image"),
          'user': self.request.get("user"),
          'price': self.request.get("price")
        }
        self.response.headers['Content-Type'] = 'text/html'
        template = env.get_template("templates/upload.html")
        self.response.write(template.render(contents)) #the response

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_db.SeedData()
        self.response.write("Seed Data Successful")

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/new', UploadPage),
    ('/init', LoadDataHandler),
], debug=True)
