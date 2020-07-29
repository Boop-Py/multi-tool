import tornado.ioloop
import tornado.web
from lib.utils import hello
from lib.username import *
from lib.password import *
from lib.conversion import *
from lib.json import *
from lib.locator import *
from lib.hash import *



class IndexHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/index.html")

class UsernameHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/username_generator.html", username = username_generator())

class PasswordHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/password_generator.html", password = password_generator())

class ConversionHandler(tornado.web.RequestHandler):
    def get(self):    
        #if top dropdown selected, show that particular form
        self.render("templates/conversions.html", temp = temp())

class JsonHandler(tornado.web.RequestHandler):
    def post(self):
        error = False
        json_input = self.get_argument("input")
        pretty = json_formatter(json_input)
        
        if pretty is None:
            error = True
        
        self.render("templates/json_formatter.html", pretty = pretty, error = error)

    def get(self):
        pretty = None
        self.render("templates/json_formatter.html", pretty = pretty)

class HashHandler(tornado.web.RequestHandler):
    def post(self):
        hash_choice = self.get_argument("hash_choice")
        input = self.get_argument("input")
        hash = hasher(hash_choice, input)
        self.render("templates/hasher.html", hash = hash)

    def get(self):
        hash = None
        self.render("templates/hasher.html", hash = hash)
        
class GeoHandler(tornado.web.RequestHandler):
    def post(self):
        ip = self.get_argument("input")
        output = geo_locator(ip)
        self.render("templates/geolocator.html", ip = output)

    def get(self):
        output = ""
        self.render("templates/geolocator.html", ip = output)

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
        (r"/username-generator", UsernameHandler),
        (r"/password-generator", PasswordHandler),
        (r"/unit-converter", ConversionHandler),
        (r"/json-formatter", JsonHandler),
        (r"/hasher", HashHandler),
        (r"/ip-geolocator", GeoHandler)
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    print("Running on port 8888")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()