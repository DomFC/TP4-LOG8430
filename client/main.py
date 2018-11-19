# inspiration
#https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a
# install python3
# pip install flask, flast_restful, pyspark and numpy using pip3
from flask import (
    Flask,
    render_template
)
import json

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('index.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
