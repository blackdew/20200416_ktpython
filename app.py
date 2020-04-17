from flask import Flask
from flask import request, redirect

app = Flask("flask")

members = [
    {"id": "sookbun", "pw": "111111"},
    {"id": "duru", "pw": "222222"},
]

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
        return template.format("")
    
    elif request.method == 'POST':
        # 만약 회원이 아니면, "회원이 아닙니다."라고 알려주자
        m = [e for e in members if e['id'] == request.form['id']]
        if len(m) == 0:
            return template.format("<p>회원이 아닙니다.</p>")
        
        # 만약 패스워드가 다르면, "패스워드를 확인해 주세요"라고 알려주자
        if request.form['pw'] != m[0]['pw']:
            return template.format("<p>패스워드를 확인해 주세요</p>")
            
        # 로그인 성공에는 메인으로
        return redirect("/")