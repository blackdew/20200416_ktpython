from flask import Flask

app = Flask(__name__)

# 자동갱신 되도록 설정
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "welcome day7 class 2222"

# python 파일명으로 실행을 위해서 필요
app.run(port=8001)