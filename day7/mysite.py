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
                           title="가장 작은 수 찾기",
                           result=result,
                           site="exam01",
                           placehoder="num1, num2, num3")

@app.route('/daum')
def daum():
    res = requests.get('http://daum.net')
    return res.text.replace('https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png', 'https://ssl.pstatic.net/sstatic/search/nlogo/20200421102755.png')

@app.route('/pub/<sub>')
def daum_sub(sub):
    res = requests.get(f'http://daum.net/pub/{sub}',
                       params=request.args)
    return res.text

# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 
# 해당 숫자에 대한 구구단을 출력하세요.
@app.route('/gugu', methods=['get', 'post'])
def gugu():
    result = ''
    if request.method == 'POST':
        number = int(request.form['numbers'].strip())
        for i in range(9):
            result += f'{number} * {i + 1} = {number * (i + 1)}<br>'
        
    return render_template('base.html', 
                           title="구구단 출력하기",
                           result=result,
                           site="gugu",
                           placehoder="num")

# python 파일명으로 실행을 위해서 필요
app.run(port=8001)