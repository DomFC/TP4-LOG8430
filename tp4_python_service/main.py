# inspiration
#https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a

from flask import (
    Flask,
    render_template
)
from flask_restful import (Api, Resource, reqparse)

# Create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')

class Hello(Resource):
    def get(self, name):
        print(name)
        return "Hello, " + name

class Words(Resource):
    def get(self, text):
        return len(str.split(text))

api.add_resource(Hello, "/hello/<string:name>")
api.add_resource(Words, "/words/<string:text>")
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)