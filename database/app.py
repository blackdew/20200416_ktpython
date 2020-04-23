import os
from flask import Flask, render_template
from flask import request, redirect, abort, session

app = Flask(__name__, 
            static_folder="static",
            template_folder="views")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.secret_key = 'sookbun'

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
    if 'user' in session:
        title = 'Welcome ' + session['user']['id']
    else:
        title = 'Welcome'
        
    content = 'Welcome Python Class...'
    menu = get_menu()
    return render_template('template.html',
                           title=title,
                           content=content,
                           menu=menu)

@app.route("/<title>")
def html(title):
    menu = get_menu()
    
    if title not in menu:
        return abort(404)

    with open(f'content/{title}', 'r') as f:
        content = f.read()

    return render_template('template.html',
                           title=title,
                           content=content,
                           menu=menu)

@app.route("/delete/<title>")
def delete(title):
    os.remove(f"content/{title}")
    return redirect("/")

@app.route("/create", methods=['GET', 'POST'])
def create():
    menu = get_menu()
    
    if request.method == 'GET':
        return render_template('create.html', 
                               message='', 
                               menu=menu)
    
    elif request.method == 'POST':
        # request.form['title'], request.form['desc']
        with open(f'content/{request.form["title"]}', 'w') as f:
            f.write(request.form['desc'])

        return redirect('/')

@app.route("/login", methods=['GET', 'POST'])
def login():
    menu = get_menu()
    
    if request.method == 'GET':
        return render_template('login.html', 
                               message="", 
                               menu=menu)
    
    elif request.method == 'POST':
        # 만약 회원이 아니면, "회원이 아닙니다."라고 알려주자
        m = [e for e in members if e['id'] == request.form['id']]
        if len(m) == 0:
            return render_template('login.html', 
                                   message="<p>회원이 아닙니다.</p>", 
                                   menu=menu)
        
        # 만약 패스워드가 다르면, "패스워드를 확인해 주세요"라고 알려주자
        if request.form['pw'] != m[0]['pw']:
            return render_template('login.html', 
                                   message="<p>패스워드를 확인해 주세요</p>", 
                                   menu=menu)
            
        # 로그인 성공에는 메인으로
        session['user'] = m[0]
        return redirect("/")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route("/favicon.ico")
def favicon():
    return abort(404)

app.run(port=8008)