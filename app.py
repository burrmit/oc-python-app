from flask import Flask
from flask import render_template
from app import app

app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Congratulations, it's a web app!"

@app.route('/templates')
def template():
    return render_template('home.html')
