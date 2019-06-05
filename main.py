# the import section
import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class HomePage(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template("templates/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

# the handler section
class UploadPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        template = env.get_template("templates/upload.html")
        self.response.write(template.render()) #the response

    def post(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        template = env.get_template("templates/upload.html")
        self.response.write(template.render()) #the response


# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/new', UploadPage)
], debug=True)
