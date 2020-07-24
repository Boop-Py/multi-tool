import tornado.ioloop
import tornado.web
from lib.utils import hello
from lib.username import *

class IndexHandler(tornado.web.RequestHandler):
    
    def post(self):
        print("posted ")
        json_input_data = self.get_argument("input")
        
        self.render("index.html", data = json_input_data)
        
    def get(self):
        data = ""
        print(hello())
        self.render("index.html", data = data)


class UsernameHandler(tornado.web.RequestHandler):
    def get(self):    
        self.render("templates/username_generator.html", username = username_generator())



def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/username-generator", UsernameHandler)
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    print("Running on port 8888")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()