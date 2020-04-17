from flask import Flask

app = Flask("flask")

@app.route("/")
def index():
    # views/index.html 에서 파일을 받아오자 
    with open('views/index.html', 'r') as f:
        html = f.read()
    
    return html