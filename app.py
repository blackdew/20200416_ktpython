from flask import Flask

app = Flask("flask")

@app.route("/")
def index():
    with open('views/template.html', 'r', encoding="utf-8") as f:
        template = f.read()
    
    return template.format('Welcome', 'Welcome Python Class...')

@app.route("/html")
def html():
    with open('views/template.html', 'r', encoding="utf-8") as f:
        template = f.read()
    
    return template.format('HTML', 'HTML is...')

@app.route("/CSS")
def css():
    with open('views/template.html', 'r', encoding="utf-8") as f:
        template = f.read()
    
    return template.format('CSS', 'CSS is...')

@app.route("/Javascript")
def javascript():
    with open('views/template.html', 'r', encoding="utf-8") as f:
        template = f.read()
    
    return template.format('Javascript', 'Javascript is...')
