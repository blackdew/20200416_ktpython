from flask import Flask

app = Flask(__name__, template_folder="templates")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    return "welcome, day8 class"

app.run(port=8000)