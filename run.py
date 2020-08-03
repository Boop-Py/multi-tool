import tornado.ioloop
import tornado.web
import argparse
from lib.username import *
from lib.password import *
from lib.json import *
from lib.locator import *
from lib.hash import *

parser = argparse.ArgumentParser()

parser.add_argument("--port",
                   action = "store",
                   type = int,
                   required = True,
                   help = "Allows you to specify the port")                 
args = parser.parse_args()                       

class IndexHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/index.html")

class UsernameHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/username_generator.html", username = username_generator())

class PasswordHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/password_generator.html", password = password_generator())

#class ConversionHandler(tornado.web.RequestHandler):
#    def get(self):    
        #if top dropdown selected, show that particular form
#        self.render("templates/conversions.html")

class JsonHandler(tornado.web.RequestHandler):
    def post(self):
        # no error as default
        error = False
        # retrieve ugly json from form
        json_input = self.get_argument("input")
        # run ugly json through function and return the easier to read json
        pretty = json_formatter(json_input)
        #return an error on the html if not json or if unavailable
        if pretty is None:
            error = True
        self.render("templates/json_formatter.html", pretty = pretty, error = error)

    def get(self):
        pretty = None
        self.render("templates/json_formatter.html", pretty = pretty)

class HashHandler(tornado.web.RequestHandler):
    def post(self):
        # no error as a default
        error = False  
        # retrieve choice and input from form
        hash_choice = self.get_argument("hash_choice")
        input = self.get_argument("input")
        try:
            # run choice + input through function
            hash = hasher(hash_choice, input)  
            # if nothing is presented, show the error message
            if hash is None:
        #if unavailable, show an error message
                error = True
        except:
            hash = None
            error = True
        self.render("templates/hasher.html", hash = hash, hash_choice = hash_choice, input = input, error = error)

    def get(self):
        hash = None
        self.render("templates/hasher.html", hash = hash)
        
class GeoHandler(tornado.web.RequestHandler):
    def post(self):
        # show no error as default
        error = False
        # retrieve ip from form 
        ip = self.get_argument("input")
        # run ip through function and return specific locations
        locations = geo_locator(ip)
        # if the IP address completely returns None, return an error 
        if locations is None:
            error = True
        self.render("templates/geolocator.html", locations = locations, error = error, ip = ip)
        
    def get(self):
        locations = None
        self.render("templates/geolocator.html", locations = locations)

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
        (r"/username-generator", UsernameHandler),
        (r"/password-generator", PasswordHandler),
        #(r"/unit-converter", ConversionHandler),
        (r"/json-formatter", JsonHandler),
        (r"/hasher", HashHandler),
        (r"/ip-geolocator", GeoHandler)
    ], debug = False)

if __name__ == "__main__":
    app = make_app()
    print("Running on port " + str(args.port))
    app.listen(args.port)
    tornado.ioloop.IOLoop.current().start()