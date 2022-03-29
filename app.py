from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route('/templates')
def template():
    return render_template('home.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)