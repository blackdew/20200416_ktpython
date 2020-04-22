from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

# 자동갱신 되도록 설정
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "welcome day7 class 2222"

@app.route("/exam01", methods=['get', 'post'])
def exam01():
    if request.method == 'POST':
        result = request.form['numbers']
        
    return render_template('base.html', 
                           result="어쩌고저쩌고")

# python 파일명으로 실행을 위해서 필요
app.run(port=8001)