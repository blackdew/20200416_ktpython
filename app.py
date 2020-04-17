from flask import Flask
from flask import request

app = Flask("flask")

def get_template(filename):
    with open('views/' + filename, 'r', encoding="utf-8") as f:
        template = f.read()
        
    return template

@app.route("/")
def index():
    template = get_template('template.html')
    return template.format('Welcome', 'Welcome Python Class...')

@app.route("/html")
def html():
    template = get_template('template.html')
    return template.format('HTML', 'HTML is...')

@app.route("/CSS")
def css():
    template = get_template('template.html')
    return template.format('CSS', 'CSS is...')

@app.route("/Javascript")
def javascript():
    template = get_template('template.html')
    return template.format('Javascript', 'Javascript is...')

@app.route("/login", methods=['GET', 'POST'])
def login():
    template = get_template('login.html')
    
    if request.method == 'GET':
        return template + "GET"
    elif request.method == 'POST':
        return template + "POST"