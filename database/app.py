import os
import pymysql
from datetime import datetime
from flask import Flask, render_template
from flask import request, redirect, abort, session, jsonify

app = Flask(__name__, 
            static_folder="static",
            template_folder="views")
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.secret_key = 'sookbun'

db = pymysql.connect(
    user='root',
    passwd='',
    host='localhost',
    db='web',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

def get_menu():
    cursor = db.cursor()
    cursor.execute("select id, title from topic")
    menu = [f"<li><a href='/{row['id']}'>{row['title']}</a></li>"
            for row in cursor.fetchall()]
    return '\n'.join(menu)

@app.route("/")
def index():    
    title = 'Welcome ' + session['user']['name'] if 'user' in session else 'Welcome'
        
    content = 'Welcome Python Class...'
    return render_template('template.html',
                           id="",
                           title=title,
                           content=content,
                           menu=get_menu())

@app.route("/<id>")
def content(id):
    cursor = db.cursor()
    cursor.execute(f"select * from topic where id = '{id}'")
    topic = cursor.fetchone()
    
    if topic is None:
        abort(404)

    return render_template('template.html',
                           id=topic['id'],
                           title=topic['title'],
                           content=topic['description'],
                           menu=get_menu())

@app.route("/delete/<id>")
def delete(id):
    cursor = db.cursor()
    cursor.execute(f"delete from topic where id='{id}'")
    db.commit()
    
    return redirect("/")

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        cursor = db.cursor() 
        sql = f"""
            insert into topic (title, description, created, author_id)
            values ('{request.form['title']}', '{request.form['desc']}',
                    '{datetime.now()}', '{session['user']['id']}')
        """
        cursor.execute(sql)
        db.commit()

        return redirect('/')
    
    return render_template('create.html', 
                           message='', 
                           menu=get_menu())

@app.route("/login", methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        cursor = db.cursor()
        cursor.execute(f"""
            select id, name, profile, password from author 
            where name = '{request.form['id']}'""")
        user = cursor.fetchone()
        
        if user is None:
            message = "<p>회원이 아닙니다.</p>"
        else:
            cursor.execute(f"""
            select id, name, profile, password from author 
            where name = '{request.form['id']}' and 
                  password = SHA2('{request.form['pw']}', 256)""")
            user = cursor.fetchone()
            
            if user is None:
                message = "<p>패스워드를 확인해 주세요</p>"
            else:
                # 로그인 성공에는 메인으로
                session['user'] = user
                return redirect("/")
    
    return render_template('login.html', 
                           message=message, 
                           menu=get_menu())

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route("/favicon.ico")
def favicon():
    return abort(404)

@app.route("/dbtest")
def dbtest():
    cursor = db.cursor()
    cursor.execute("select * from topic")
    return str(cursor.fetchall())

######################
## restful API

@app.route("/api/author", methods=['get', 'post'])
def author_list():
    cursor = db.cursor()
    
    if request.method == 'GET':
        cursor.execute("select * from author")    
        return jsonify(cursor.fetchall())
    elif request.method == 'POST':
        sql = f"""insert into author (name, profile, password)
                  values ('{request.form['name']}', '{request.form['profile']}',
                  SHA2('{request.form['password']}', 256))"""
        cursor.execute(sql)
        db.commit()
        
        return jsonify({"success": True})
    
    return abort(405)

@app.route("/api/author/<author_id>", methods=['get', 'put', 'delete'])
def author(author_id):
    cursor = db.cursor()
    
    if methods == 'GET':
        cursor.execute(f"select * from author where id = {author_id}")
        author = cursor.fetchone()

        if author:
            return jsonify(author)
        else:
            return abort(404)
    elif methods == 'PUT':
        return jonify({"success": True})
    elif methods == 'DELETE':
        return jonify({"success": True})
    
    return abort(405)


app.run(port=8008)