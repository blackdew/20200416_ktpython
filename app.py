from flask import Flask

app = Flask("flask")

@app.route("/")
def index():
    # views/index.html 에서 파일을 받아오자 
    with open('views/index.html', 'r') as f:
        html = f.read()
    
    return html

@app.route("/html")
def html():
    # views/index.html 에서 파일을 받아오자 
    with open('views/1.html', 'r') as f:
        html = f.read()
    
    return html

@app.route("/CSS")
def css():
    # views/index.html 에서 파일을 받아오자 
    with open('views/2.html', 'r') as f:
        html = f.read()
    
    return html

@app.route("/Javascript")
def javascript():
    # views/index.html 에서 파일을 받아오자 
    with open('views/3.html', 'r') as f:
        html = f.read()
    
    return html
