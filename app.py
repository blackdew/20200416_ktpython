import os
from flask import Flask
from flask import request, redirect

app = Flask("flask")

members = [
    {"id": "sookbun", "pw": "111111"},
    {"id": "duru", "pw": "222222"},
]

def get_menu():
    menu_temp = "<li><a href='/{0}'>{0}</a></li>"
    menu = [e for e in os.listdir('content') if e[0] != '.']
    return "\n".join([menu_temp.format(m) for m in menu])

def get_template(filename):
    with open('views/' + filename, 'r', encoding="utf-8") as f:
        template = f.read()
        
    return template

@app.route("/")
def index():
    id = request.args.get('id', '')
    template = get_template('template.html')
    
    title = 'Welcome ' + id
    content = 'Welcome Python Class...'
    menu = get_menu()
    return template.format(title, content, menu)

@app.route("/<title>")
def html(title):
    template = get_template('template.html')
    menu = get_menu()

    with open(f'content/{title}', 'r') as f:
        content = f.read()

    return template.format(title, content, menu)

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
        return redirect("/?id=" + m[0]['id'])