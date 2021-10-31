#Import the flask dependency
from flask import Flask
#create a new flask app instance
app = Flask(__name__)
#create flask routes
@app.route('/')
def hello_world():
    a = input("what's your favorite food?")
    return a