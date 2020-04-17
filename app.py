from flask import Flask

app = Flask("flask")

@app.route("/")
def index():
    with open('views/index.html', 'r', encoding="utf-8") as f:
        html = f.read()
    
    return html

@app.route("/html")
def html():
    with open('views/1.html', 'r', encoding="utf-8") as f:
        html = f.read()
    
    return html

@app.route("/CSS")
def css():
    with open('views/2.html', 'r', encoding="utf-8") as f:
        html = f.read()
    
    return html

@app.route("/Javascript")
def javascript():
    with open('views/3.html', 'r', encoding="utf-8") as f:
        html = f.read()
    
    return html
