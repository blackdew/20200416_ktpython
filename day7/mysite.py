import requests
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
    result = ''
    if request.method == 'POST':
        result = request.form['numbers']
        result = [int(s.strip()) for s in result.split(',')]
        min_number = min(result)
        
        if min_number % 2 == 0:
            result = f'가장 작은 수 {min_number}는 짝수'
        else:
            result = f'가장 작은 수 {min_number}는홀수'
        
    return render_template('base.html', 
                           result=result)

@app.route('/daum')
def daum():
    res = requests.get('http://daum.net')
    return res.text

@app.route('/pub/<sub>')
def daum_sub(sub):
    res = requests.get(f'http://daum.net/pub/{sub}',
                       params=request.args)
    return res.text
    

# python 파일명으로 실행을 위해서 필요
app.run(port=8001)